import datetime

from pyconomic import base
from pyconomic import models


class VatZone:
    Domestic = "HomeCountry"
    EU = "EU"
    Abroad = "Abroad"


class EconomicsFacade(object):
    def __init__(self, client, service):
        self.client = client
        self.service = service

    def _build_types(self):
        modelcode = base.build_model_code(self.client)
        exec modelcode in globals()
        return modelcode

    def initialize(self, url, agreement_number, user_id, password):
        conf = {
            'agreementNumber': str(agreement_number),
            'userName': user_id,
            'password': password
        }
        self.service.Connect(**conf)

    def get_all_changes(self):
        return self.service.get_all_changes()

    def commit(self):
        self.service.commit()

    def find(self, model, **spec):
        return self.service.find(model, **spec)

    def get(self, model, **spec):
        return self.service.get(model, **spec)

    def get_or_create(self, model, **spec):
        """
        Args:
            model: class of Model
            get_data: the filter used for finding an instance
            create_data: the data used to create an instance, if none could be found
        """
        return self.service.get_or_create(model, **spec)

    def create(self, model, **data):
        return self.service.create(model, **data)

    def num_server_calls(self):
        return self.service.ncalls

    def send_order(self, order):
        self.service.fetch('Order_RegisterAsSent', order._handle)

    def create_order(self, debtor, is_vat_included=True, due_date=None,
                     heading='', text_line1='', text_line2='',
                     debtor_data=None, delivery_data=None, products=None,
                     project=None, other_reference='', model=models.Order, **extra
                     ):
        """Create a new Order.

        Args:
            debtor (Debtor): the debtor of the order
            debtor_data (mapping): map of debtor data {'postal_code: .., 'city': .., 'ean': ..}
                                   defaults to values on debitor instance for missing values
            delivery_data (mapping): map of delivery data {'address': ..., 'postal_code': ...}
                                     defaults to values on debitor instance for missing values
            due_date (datetime): due date
            heading (string): heading to be displayed in the order pdf
            text_line1 (string): first order description line
            text_line2 (string): second order description line
            other_reference (string): custom string to be used for identification
            extra (mapping): mapping of extra values to be passed in to the server call
        Returns:
            Order instance
        """

        debtor_data = debtor_data or {}
        delivery_data = delivery_data or {}
        delivery_date = delivery_data.get('date', datetime.datetime.now())
        our_reference = extra.get('our_reference', debtor.our_reference)
        currency = extra.get('currency', debtor.currency)
        layout = extra.get('layout', debtor.layout)
        term_of_payment = extra.get('term_of_payment', debtor.term_of_payment)
        date = extra.get('date', datetime.datetime.now())
        order_input = {
            'debtor': debtor,
            'number': extra.get('number', 1),
            'project': project,
        }
        for dd in ['name', 'address', 'postal_code', 'city', 'country', 'ean']:
            order_input['debtor_%s' % dd] = debtor_data.get(dd, getattr(debtor, dd))

        for dd in ['address', 'postal_code', 'city', 'country']:
            order_input['delivery_%s' % dd] = delivery_data.get(dd, getattr(debtor, dd))

        order_input.update({
            'delivery_date': delivery_date or datetime.datetime.now(),
            'heading': heading,
            'text_line1': text_line1,
            'text_line2': text_line2,
            'is_archived': extra.get('is_archived', 0),
            'is_sent': extra.get('is_sent', 0),
            'net_amount': extra.get('net_amount', 0),
            'vat_amount': extra.get('vat_amount', 0),
            'gross_amount': extra.get('gross_amount', 0),
            'margin': extra.get('margin', 0),
            'margin_as_percent': extra.get('margin_as_percent', 0),
            'date': date,
            'our_reference': our_reference,
            'other_reference': other_reference,
            'currency': currency,
            'exchange_rate': extra.get('exchange_rate', 1.0),
            'is_vat_included': is_vat_included,
            'layout': layout,
            'due_date': due_date or datetime.datetime.now(),
            'term_of_payment': term_of_payment
        })
        order_input.update(extra)
        order = self.create(model, **order_input)
        if products:
            for product in products:
                self.create_orderline(order, product)
        return order

    def create_orderline(self, order, product, quantity=1, description=None, number=1,
                         unit_net_price=None, unit_cost_price=None, total_net_amount=None, discount_as_percent=0,
                         delivery_date=None, total_margin=0, margin_as_percent=0, model=models.OrderLine
                         ):
        delivery_date = delivery_date or datetime.datetime.now()
        unit_net_price = unit_net_price or product.sales_price
        unit_cost_price = unit_cost_price or product.cost_price
        total_net_amount = total_net_amount or product.sales_price
        description = product.description if description is None else description

        line_input = {
            'order': order,
            'product': product,
            'number': number,
            'description': description,
            'delivery_date': delivery_date,
            'quantity': quantity,
            'unit_net_price': unit_net_price,
            'unit_cost_price': unit_cost_price,
            'total_net_amount': total_net_amount,
            'discount_as_percent': discount_as_percent,
            'total_margin': total_margin,
            'margin_as_percent': margin_as_percent
        }
        return self.create(model, **line_input)

    def create_product(self, number, product_group, name, sales_price, description='', cost_price=0.0,
                       in_stock=100.0, recommended_price=0.0, distribution_key=None,
                       volume=100.0, department=None, available=0.0, is_accessible=True,
                       unit=None, bar_code='', on_order=0.0, model=models.Product
                       ):

        product_input = {
            'distribution_key': distribution_key,
            'department': department,
            'product_group': product_group,
            'unit': unit,

            'number': number,

            'on_order': on_order,
            'name': name,
            'sales_price': sales_price,
            'description': description,
            'cost_price': cost_price,
            'in_stock': in_stock,
            'recommended_price': recommended_price,
            'volume': volume,
            'available': available if available is not None else in_stock,
            'bar_code': bar_code,
            'is_accessible': is_accessible
        }
        return self.create(model, **product_input)

    def create_debtor(self, debtor_group, name, term_of_payment, vat_zone, currency,
                      number=None, is_accessible=True, model=models.Debtor, **extra):
        if number is None:
            number = self.service.next_available_number(model)
        debtor_input = {
            'name': name,
            'number': number,
            'debtor_group': debtor_group,
            'term_of_payment': term_of_payment,
            'vat_zone': vat_zone,
            'currency': currency,
            'is_accessible': is_accessible
        }
        debtor_input.update(extra)
        return self.create(model, **debtor_input)

    def upgrade_to_invoice(self, order, model=models.CurrentInvoice):
        return self.service.upgrade_to_invoice(order._handle, model)

    def upgrade_to_order(self, quotation, model=models.Order):
        return self.service.upgrade_to_order(quotation._handle, model)

    def book_invoice(self, current_invoice, model=models.Invoice):
        return self.service.book_invoice(current_invoice._handle, model)

    def find_orders(self):
        pass

    def find_invoices(self):
        pass

    def find_accounts(self):
        pass


def Pyconomic(agreement_number, user_id, password):
    url = 'https://api.e-conomic.com/secure/api1/EconomicWebservice.asmx?WSDL'
    model_factory = base.EConomicsModelFactory()
    wsdl = base.Client(url)
    codec = base.PropertyCodec()
    service = base.EConomicsService(wsdl.service, model_factory, wsdl.factory, codec)
    
    facade = EconomicsFacade(wsdl, service)
    facade.initialize(
        url,
        agreement_number, user_id, password
    )
    return facade