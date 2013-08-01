pyconomics is a python client/abstraction for the e-conomic API (e-conomic.com)


Installation
------------

Install SUDS:
 pip install suds


pip install pyconomic


Basic Usage
-----------

    # startup
    >>> import pyconomic
    >>> from pyconomic import models
    >>> pycon = pyconomic.Pyconomic(agreement_nr, user_id, password)

    # get / create base models
    >>> random_account = pycon.find(models.DebtorGroup)[0].account
    >>> terms = pycon.get(models.TermOfPayment, name='Net 8 days')
    >>> debtor_group = pycon.get_or_create(models.DebtorGroup, name='Test Group', number=123, account=random_account)
    >>> currency = pycon.get_or_create(models.Currency, code='DKK')

    # create debtor - you can also use "pycon.create(models.Debtor, ..)", all "create_" methods are facade methods to help construct all the input
    >>> john = pycon.create_debtor(debtor_group, 'John Doe', terms, pyconomic.VatZone.Domestic, currency, address='Somewhere', city='LongAgo', country='FarFarAway')

    # pyconomic will cache all instances, so the john-instance should be in the any new query of debtors from the server
    >>> debtors = pycon.find(models.Debtor, partial_name='John*')
    >>> john in debtors and debtors[0].name == 'John Doe'
    True

    # create products
    >>> product_group = pycon.find(models.ProductGroup)[0]  # use a random product group
    >>> service = pycon.create_product('1000', product_group, 'Consulting Service', 300, description='I Do Stuff')
    >>> thing = pycon.create_product('1001', product_group, 'Thing', 1200, description='Thing in black')

    # create orders
    >>> order1 = pycon.create_order(john, products=[service, thing])

    # first time accessing a list-property like "orders" will do a server-call, and cache result for next access
    >>> john.orders
    [<Order ...>]

    # which means that any new orders will not show up on the orders property
    >>> order2 = pycon.create_order(john, products=[thing])
    >>> len(john.orders)
    1

    # use fetch to ask the server for new data
    >>> john.orders.fetch()
    [<Order ...>, <Order ...>]
    >>> len(john.orders)
    2

    # instances also has a fetch.. Reload the product data of the first order-line in the first of johns orders (for the fun of it):
    >>> john.orders[0].lines[0].product.fetch()
    <Product ...>

    # updating data - pycon.commit() will send all changes to server
    >>> orderline = john.orders[0].lines[0]
    >>> orderline.quantity = 3
    >>> pycon.get_all_changes()[models.OrderLine]
    [<Changes <OrderLine ...> {'quantity': 3}>]
    >>> pycon.commit()
    >>> pycon.get_all_changes()[models.OrderLine]
    []
    >>> orderline.quantity
    3

    # upgrade order to invoice (must not be sent)
    >>> pycon.upgrade_to_invoice(order1)
    <CurrentInvoice ...>

    # send order
    >>> order2.is_sent
    False
    >>> pycon.send_order(order2)
    >>> order2.fetch().is_sent
    True

    # save order-pdf to the file "orderpdf.pdf" in the current working directory
    >>> order2.pdf.save('orderpdf')

    # delete everything again, orders seems be deleted as the debtor is deleted
    >>> john.delete()
    >>> service.delete()
    >>> thing.delete()


Notes
-----

* Model instances are cached and reused based on their handle
* The "find", "get", and "get_or_create" requires available "TYPE_FindBy[X]" server-method, and will make multiple server-calls if needed
* Once a single instance needs its data, it will fetch the data of all instances in the cache by that type
* List properties require a separate server-call:
   [debtor.invoices for debtor in debtors] would be as many server-calls as there's debtors, while getting attribute "name" is only 1 server-call to get all names
* Changes in data is only saved on pycon.commit() except for Create and Delete which saves immediately

To-Do
-----

* add "updated since" query
* create more facade methods, only has a few (create_order, create_products, ...) - use pycon.create([Model], **arguments) for the rest
* update cache on create; doing create_orderline should update all the "order.lines" properties - use ".fetch()" to update data instead
* properties are missing a "read_only" state, so the user wont try to change data that cannot be saved
* see if possible to create a data-model that is more IDE auto-complete friendly
* add missing enums, only got for VatZone
*