"""
Model Abstraction of e-economic.com API
"""

import copy
import re
import os
import base64
from collections import defaultdict

from suds.client import Client


class ObjectDoesNotExist(BaseException):
    pass


class MultipleObjectsReturned(BaseException):
    pass


class EConomicsService(object):
    """
    Interface for e-conomic WSDL service
    """
    def __init__(self, service, model_factory, soap_factory, codec):
        self.service = service
        self.model_factory = model_factory
        self.soap_factory = soap_factory
        self.ncalls = 0
        self.codec = codec

    def fetch_list(self, name, expected_wsdltype, *args, **kw):
        result = getattr(self.service, name)(*args)
        self.ncalls += 1
        if not result:
            return []
        if expected_wsdltype and expected_wsdltype not in result.__keylist__:
            return [result]
        return result[0]

    def fetch(self, name, *args, **kw):
        return getattr(self.service, name)(*args)

    def upgrade_to_order(self, handle, order_model):
        hnd = self.fetch('Quotation_UpgradeToOrder', handle)
        return self.model_factory.get_or_create_instance(self, order_model, hnd)

    def upgrade_to_invoice(self, handle, current_invoice_model):
        hnd = self.fetch('Order_UpgradeToInvoice', handle)
        return self.model_factory.get_or_create_instance(self, current_invoice_model, hnd)

    def book_invoice(self, handle, invoice_model):
        hnd = self.fetch('CurrentInvoice_Book', handle)
        return self.model_factory.get_or_create_instance(self, invoice_model, hnd)

    def next_available_number(self, model):
        return self.fetch('%s_GetNextAvailableNumber' % model.__name__)

    def delete(self, model, handle):
        self.fetch("%s_Delete" % model.__name__, handle)

    def create(self, model, **data):
        parsed_data = self.codec.encode_data_object(self, model, data)
        hnd = self.fetch("%s_CreateFromData" % model.__name__, parsed_data)
        return self.get_instance(model, hnd)

    def get_or_create(self, model, **spec):
        filter_names = [f['name'] for f in model.__filters__]
        get_data = dict((k, v,) for k, v in spec.items() if k in filter_names)
        try:
            return self.get(model, **get_data)
        except ObjectDoesNotExist:
            return self.create(model, **spec)

    def __find_handles(self, model, **spec):
        """ find model instances based on given filter (spec)
        The filter is based on available server-calls, so some values might not be available for filtering.
        Multiple filter-values is going to do multiple server-calls.
        For complex filters in small datasets, it might be faster to fetch all and do your own in-memory filter.
        Empty filter will fetch all.

        :param model: subclass of EConomicsModel
        :param spec: mapping of values to filter by
        :return: a list of EConomicsModel instances
        """
        server_calls = []
        filter_names = dict([(f['name'], f['method'],) for f in model.get_filters()])
        if not spec:
            server_calls.append({'method': "%s_GetAll" % model.__name__, 'args': []})
        else:
            for key, value in spec.items():
                if not key in filter_names:
                    raise ValueError("no server-method exists for filtering by '%s'" % key)
                args = []
                if not hasattr(value, '__iter__'):
                    value = [value]

                if key.endswith('_list'):
                    vtype = type(value[0]).__name__
                    # TODO: this surely does not cover all cases of data types
                    array = self.soap_factory.create('ArrayOf%s' % vtype.capitalize())
                    getattr(array, "%s" % vtype).extend(value)
                    args.append(array)
                else:
                    args.extend(value)

                method = "%s_%s" % (model.__name__, filter_names[key])
                if filter_names[key].startswith('GetAll'):
                    args = []
                server_calls.append({'method': method, 'args': args, 'expect': "%sHandle" % model.__name__})

        handles = [
            map(Handle, self.fetch_list(scall['method'], scall.get('expect'), *scall['args']))
            for scall in server_calls
        ]
        return [h.wsdl for h in reduce(set.intersection, map(set, handles))]

    def find(self, model, **spec):
        handles = self.__find_handles(model, **spec)
        return [self.get_instance(model, hnd) for hnd in handles]

    def get(self, model, **spec):
        """get a single model instance by handle

        :param model: model
        :param handle: instance handle
        :return:
        """

        handles = self.__find_handles(model, **spec)
        if len(handles) > 1:
            raise MultipleObjectsReturned()
        if not handles:
            raise ObjectDoesNotExist()
        return self.get_instance(model, handles[0])

    def get_instance(self, model, handle):
        return self.model_factory.get_or_create_instance(self, model, handle)

    def load_instance_data(self, instance):
        model = instance.__class__
        modelname = model.__name__
        data = self.fetch("%s_GetData" % modelname, instance._handle)
        instance._data = self.codec.decode_data_object(self, instance._handle, model, data)

    def load_data(self, instance):
        model = instance.__class__
        modelname = model.__name__
        handles = [inst._handle for (m, inst,) in self.model_factory.instances_iter([model], loaded=False)]
        array = self.soap_factory.create('ArrayOf%sHandle' % modelname)
        getattr(array, "%sHandle" % modelname).extend(handles)

        for data in self.fetch_list("%s_GetDataArray" % modelname, None, array):
            handle = data.Handle
            inst = self.get_instance(model, handle)
            inst._data = self.codec.decode_data_object(self, handle, model, data)
            inst._loaded = True

    def get_all_changes(self):
        changesets = defaultdict(list)
        for model, inst in self.model_factory.instances_iter(updated=True):
            changesets[model].append(ModelChange(model, inst))
        return changesets

    def commit(self):
        changesets = self.get_all_changes()
        for model, changes in changesets.items():
            datalist = [self.codec.encode_data_object(self, model, changeset.get_data()) for changeset in changes]
            array = self.soap_factory.create('ArrayOf%sData' % model.__name__)
            getattr(array, '%sData' % model.__name__).extend(datalist)

            self.fetch("%s_UpdateFromDataArray" % model.__name__, array)
            [change.apply_and_clear() for change in changes]

    def __getattr__(self, name):
        return getattr(self.service, name)


class ModelChange(object):
    def __init__(self, model, instance):
        self.model = model
        self.instance = instance

    def __repr__(self):
        return "<Changes %r %r>" % (self.instance, self.clean_data(self.instance._changes))

    def apply_and_clear(self):
        self.instance._data.update(self.instance._changes)
        self.instance._changes = {}

    def clean_data(self, data):
        result = {}
        for k, v in data.items():
            k = pythonize(k)
            if k.endswith('_handle'):
                k = k[:-7]
            result[k] = v
        return result

    def get_data(self):
        if not self.instance._data:
            self.instance.fetch()
        data = self.clean_data(self.instance._data)
        data.update(self.clean_data(self.instance._changes))
        data['Handle'] = self.instance._handle
        return data


class PropertyCodec(object):
    def __init__(self, missing_value=None):
        self.missing_value = missing_value

    def decode_data_object(self, service, handle, model, data):
        decoded_data = {}
        for prop in model.properties:
            name = prop.name
            if prop.name+'Handle' in data:
                name = prop.name + 'Handle'
            if not name in data:
                value = prop.default_value(service, handle)
            else:
                value = prop.decode_value(service, handle, data[name])
            decoded_data[prop.name] = value
        return decoded_data

    def encode_data_object(self, service, model, data):
        #print 'ENCODE', data
        encoded_data = {}
        if 'Handle' in data:
            encoded_data['Handle'] = data['Handle']
        for prop in model.properties:
            name = prop.pyname
            if not name in data:
            #    encoded_data[prop.name] = self.missing_value
                continue
            value = data[name]
            if value is None:
            #    encoded_data[prop.name] = value
                continue
            encoded_data[prop.name] = prop.encode_value(service, data[name])
        return encoded_data


class EConomicsModelFactory(object):
    def __init__(self):
        self.__models = {}

    def instances_iter(self, models=None, loaded=None, updated=None):
        if models is None:
            models = self.__models.keys()
        for model in models:
            for inst in self.__models[model].values():
                if loaded is not None and bool(inst._loaded) != bool(loaded):
                    continue
                if updated is not None and bool(inst._changes) != bool(updated):
                    continue
                yield (model, inst,)

    def get_or_create_instance(self, service, model, handle):
        hashkey = hash((service, model, handle[0],))
        modeldata = self.__models.setdefault(model, {})
        return modeldata.setdefault(hashkey, model(service, handle))


class Handle(object):
    def __init__(self, wsdl):
        self.wsdl = wsdl

    def __hash__(self):
        return hash(self.wsdl[0])

    def __eq__(self, other):
        return hash(self) == other

    def __repr__(self):
        return "<Handle %r>" % self.wsdl.Id


class EConomicsMeta(type):
    registry = {}

    def __new__(mcs, name, bases, ns):
        properties = []
        for k, v in ns.items():
            if hasattr(v, '__get__'):
                properties.append(v)
        ns['properties'] = properties
        model = type.__new__(mcs, name, bases, ns)

        mcs.registry[name] = model
        return model

    def get_filters(self):
        return self.__filters__


class EConomicsBaseProperty(object):
    def encode_value(self, service, value):
        return value

    def decode_value(self, service, handle, value):
        return value

    def default_value(self, service, handle):
        return None

    def __get__(self, instance, owner):
        _ = owner
        if instance is None:
            return self

        changes = instance._changes
        if self.name in changes:
            return changes[self.name]

        if not instance._loaded:
            instance.load()

        value = instance._data[self.name]
        if hasattr(value, 'fetched') and not value.fetched:
            value.fetch()

        return value

    def __set__(self, instance, value):
        instance._changes[self.name] = value


class EConomicsProperty(EConomicsBaseProperty):
    def __init__(self, name):
        self.name = name
        self.pyname = pythonize(name)

    def __repr__(self):
        return "<%s Data>" % pythonize(self.name)


class EConomicsReference(EConomicsBaseProperty):
    def __init__(self, name, model):
        self.name = name + 'Handle'
        self.model = model
        self.pyname = pythonize(name)

    def encode_value(self, service, value):
        return value._handle

    def decode_value(self, service, handle, value):
        return service.get_instance(get_model(self.model), value)

    def __repr__(self):
        return "<%s %s>" % (self.name, self.model)


class QueryList(list):
    def __init__(self, service, handle, model, method):
        self.service = service
        self.handle = handle
        self.model = model
        self.method = method
        self.fetched = False

    def __getattribute__(self, name):
        if name in ['fetch', 'service', 'handle', 'model', 'method', 'fetched']:
            return list.__getattribute__(self, name)
        if self.fetched:
            self.fetch()
        return list.__getattribute__(self, name)

    def fetch(self):
        handles = self.service.fetch_list(self.method, None, self.handle)
        self[:] = [self.service.get_instance(self.model, hnd) for hnd in handles]
        self.fetched = True
        return self


class EConomicsReferenceList(EConomicsBaseProperty):
    def __init__(self, name, model, method):
        self.name = name
        self.model = model
        self.method = method
        self.pyname = pythonize(name)

    def __repr__(self):
        return "<%s [%s]>" % (self.name, self.model)

    def encode_value(self, service, value):
        return [v._handle for v in value]

    def default_value(self, service, handle):
        return QueryList(service, handle, get_model(self.model), self.method)


class EConomicsFileProperty(EConomicsBaseProperty):
    def __init__(self, name, method, filetype):
        self.name = name
        self.filetype = filetype
        self.method = method
        self.pyname = pythonize(name)

    def __repr__(self):
        return "<%s %s file>" % (self.name, self.filetype)

    def default_value(self, service, handle):
        return FileObject(service, self.method, handle, self.filetype)


class FileObject(object):
    def __init__(self, service, method, handle, filetype):
        self.filedata = None
        self.method = method
        self.service = service
        self.handle = handle
        self.filetype = filetype
        self.fetched = False
        self.__last_location = None

    def fetch(self):
        self.filedata = self.service.fetch(self.method, self.handle)
        self.fetched = True
        return self

    def save(self, location):
        if not location.endswith(self.filetype):
            location += '.' + self.filetype
        with open(location, 'wb') as f:
            f.write(base64.b64decode(self.filedata))
        self.__last_location = location

    def show(self):
        if not self.__last_location:
            self.save('/tmp/economic_tmp')
        os.system('xdg-open %s' % self.__last_location)


class EConomicsModel(object):
    __filters__ = []
    __metaclass__ = EConomicsMeta

    def __init__(self, service, handle):
        self._handle = handle
        self._loaded = False
        self._service = service
        self._data = {}
        self._changes = {}

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self._handle[0])

    def fetch(self):
        self._service.load_instance_data(self)
        return self

    def update(self, **data):
        for k, v in data.items():
            setattr(self, k, v)

    def load(self):
        self._service.load_data(self)

    def delete(self):
        self._service.delete(self.__class__, self._handle)


def get_model(name):
    return EConomicsMeta.registry[name]


def pythonize(name):
    return re.sub('([A-Z])([a-z])', r'_\1\2', name).strip('_').lower()


def camelcase(name):
    return ''.join(map(str.capitalize, name.split('_')))


def build_model_code(client):
    """
    Generate source code for e-conomic models based on WSDL connection.
    This is based on the assumption that the API follows a specific method naming-convention.
    Not all models and attributes has been tested.
    The source-generation is mostly to help improve readability and IDE auto-completion.

    :param client:
    :return: source code for models.py
    """
    models = {}
    references = {}
    for method in client.wsdl.services[0].ports[0].methods.values():
        if not '_' in method.name:
            continue
        model, action = method.name.split('_')
        models.setdefault(model, {'properties': [], 'filters': []})
        references[model] = model
        if model[-1] == 'y':
            references[model[:-1] + 'ies'] = model
        else:
            references[model+'s'] = model

    references['OurReference'] = 'Employee'
    references['GetYourReference'] = 'DebtorContact'
    references['GetAttention'] = 'DebtorContact'
    references['Layout'] = 'TemplateCollection'
    special = {
        'Order_GetPdf': {
            'type': 'EConomicsFileProperty',
            'args': ["'Order_GetPdf'", "'pdf'"]
        },
        'Invoice_GetPdf': {
            'type': 'EConomicsFileProperty',
            'args': ["'Invoice_GetPdf'", "'pdf'"]
        },
        'CurrentInvoice_GetPdf': {
            'type': 'EConomicsFileProperty',
            'args': ["'CurrentInvoice_GetPdf'", "'pdf'"]
        }
    }
    for line in ['Order', 'Invoice', 'CurrentInvoice', 'Quotation']:
        method = '%s_GetLines' % line
        special[method] = {
            'type': 'EConomicsReferenceList',
            'args': ["'%sLine'" % line, "'%s'" % method]
        }

    for method in client.wsdl.services[0].ports[0].methods.values():
        if not '_' in method.name:
            continue
        model, action = method.name.split('_')
        if action in ['GetData', 'GetAll', 'GetDataArray']:
            continue
        modeldata = models[model]

        if action == 'GetAllUpdated':
            camelname = action[3:]
            modeldata['filters'].append({'name': pythonize(camelname), 'method': action})
        if re.findall('GetAll[A-Z].+', action):
            camelname = action[3:]
            modeldata['filters'].append({'name': pythonize(camelname), 'method': action})
        elif action.startswith('FindBy'):
            camelname = action[6:]
            modeldata['filters'].append({'name': pythonize(camelname), 'method': action})

        elif action.startswith('Get'):
            propname = action[3:]
            pyname = pythonize(propname)
            if not propname:
                continue
            get_type = re.findall('Get(%s)[a-z0-9]*?$' % ('|'.join(references.keys())), action)
            if get_type and get_type[0] in references:
                refmodel = references[get_type[0]]
                if action[-1] == 's':
                    modeldata['properties'].append({
                        'type': 'EConomicsReferenceList',
                        'args': ["'%s'" % propname, "'%s'" % refmodel,  "'%s'" % method.name],
                        'name': pyname
                    })
                else:
                    modeldata['properties'].append({
                        'type': 'EConomicsReference',
                        'args': ["'%s'" % propname, "'%s'" % refmodel],
                        'name': pyname
                    })
            elif method.name in special:
                spdata = special[method.name]
                modeldata['properties'].append({
                    'type': spdata['type'],
                    'args': ["'%s'" % propname] + spdata['args'],
                    'name': pyname
                })
            else:
                modeldata['properties'].append({
                    'type': 'EConomicsProperty',
                    'args': ["'%s'" % propname],
                    'name': pyname
                })

    classes = []
    for modelname, modeldata in models.items():

        propertycode = ["%s = %s(%s)" % (md['name'], md['type'], ', '.join(md['args']))
                        for md in modeldata['properties']]
        code = "class %s(%s):\n    __filters__ = %r\n    %s" % (modelname, 'EConomicsModel',
                                                                modeldata['filters'], '\n    '.join(propertycode))
        classes.append(code)
    return "from pyconomic.base import *\n\n\n" + "\n\n\n".join(classes)
