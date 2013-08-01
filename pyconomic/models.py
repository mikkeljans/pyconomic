from pyconomic.base import *


class AccountingPeriod(EConomicsModel):
    __filters__ = [{'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    from_date = EConomicsProperty('FromDate')
    status = EConomicsProperty('Status')
    to_date = EConomicsProperty('ToDate')
    period = EConomicsProperty('Period')
    accounting_year = EConomicsReference('AccountingYear', 'AccountingYear')


class CostTypeGroup(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}]
    account_closed = EConomicsProperty('AccountClosed')
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')
    account_ongoing = EConomicsProperty('AccountOngoing')


class DebtorEntry(EConomicsModel):
    __filters__ = [{'name': u'invoice_number', 'method': u'FindByInvoiceNumber'}, {'name': u'serial_number', 'method': u'FindBySerialNumber'}]
    invoice_number = EConomicsProperty('InvoiceNumber')
    remainder = EConomicsProperty('Remainder')
    due_date = EConomicsProperty('DueDate')
    amount = EConomicsProperty('Amount')
    serial_number = EConomicsProperty('SerialNumber')
    currency = EConomicsReference('Currency', 'Currency')
    type = EConomicsProperty('Type')
    text = EConomicsProperty('Text')
    account = EConomicsReference('Account', 'Account')
    date = EConomicsProperty('Date')
    amount_default_currency = EConomicsProperty('AmountDefaultCurrency')
    remainder_default_currency = EConomicsProperty('RemainderDefaultCurrency')
    debtor = EConomicsReference('Debtor', 'Debtor')
    voucher_number = EConomicsProperty('VoucherNumber')


class Creditor(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    number = EConomicsProperty('Number')
    our_reference = EConomicsReference('OurReference', 'Employee')
    city = EConomicsProperty('City')
    term_of_payment = EConomicsReference('TermOfPayment', 'TermOfPayment')
    entries = EConomicsReferenceList('Entries', 'Entry', 'Creditor_GetEntries')
    default_payment_type = EConomicsProperty('DefaultPaymentType')
    creditor_contacts = EConomicsReferenceList('CreditorContacts', 'CreditorContact', 'Creditor_GetCreditorContacts')
    creditor_group = EConomicsReference('CreditorGroup', 'CreditorGroup')
    currency = EConomicsReference('Currency', 'Currency')
    ci_number = EConomicsProperty('CINumber')
    is_accessible = EConomicsProperty('IsAccessible')
    vat_zone = EConomicsProperty('VatZone')
    open_entries = EConomicsProperty('OpenEntries')
    default_payment_creditor_id = EConomicsProperty('DefaultPaymentCreditorId')
    name = EConomicsProperty('Name')
    entries_by_invoice_no = EConomicsProperty('EntriesByInvoiceNo')
    address = EConomicsProperty('Address')
    email = EConomicsProperty('Email')
    entries_by_voucher_no_and_invoice_no = EConomicsProperty('EntriesByVoucherNoAndInvoiceNo')
    bank_account = EConomicsProperty('BankAccount')
    auto_contra_account = EConomicsProperty('AutoContraAccount')
    entries_by_voucher_no = EConomicsProperty('EntriesByVoucherNo')
    country = EConomicsProperty('Country')
    county = EConomicsProperty('County')
    your_reference = EConomicsProperty('YourReference')
    attention = EConomicsProperty('Attention')
    postal_code = EConomicsProperty('PostalCode')


class ExtendedVatZone(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}]
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class CostType(EConomicsModel):
    __filters__ = [{'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'name', 'method': u'FindByName'}]
    vat_account = EConomicsReference('VatAccount', 'VatAccount')
    number = EConomicsProperty('Number')
    name = EConomicsProperty('Name')
    cost_type_group = EConomicsReference('CostTypeGroup', 'CostTypeGroup')


class TemplateCollection(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}]
    name = EConomicsProperty('Name')


class BudgetFigure(EConomicsModel):
    __filters__ = [{'name': u'date', 'method': u'FindByDate'}]
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    text = EConomicsProperty('Text')
    to_date = EConomicsProperty('ToDate')
    account = EConomicsReference('Account', 'Account')
    from_date = EConomicsProperty('FromDate')
    amount_default_currency = EConomicsProperty('AmountDefaultCurrency')
    department = EConomicsReference('Department', 'Department')


class DistributionKey(EConomicsModel):
    __filters__ = [{'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}]
    number = EConomicsProperty('Number')
    percentages = EConomicsProperty('Percentages')
    departments = EConomicsReferenceList('Departments', 'Department', 'DistributionKey_GetDepartments')
    name = EConomicsProperty('Name')
    is_accessible = EConomicsProperty('IsAccessible')


class ReportCodeSet(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}]
    code_set = EConomicsProperty('CodeSet')
    name = EConomicsProperty('Name')
    codes = EConomicsProperty('Codes')


class ProductGroup(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'name', 'method': u'FindByName'}]
    accrual = EConomicsProperty('Accrual')
    name = EConomicsProperty('Name')
    account_for_vat_exempt_debtor_invoices_current = EConomicsProperty('AccountForVatExemptDebtorInvoicesCurrent')
    products = EConomicsReferenceList('Products', 'Product', 'ProductGroup_GetProducts')
    account_for_vat_liable_debtor_invoices_current = EConomicsProperty('AccountForVatLiableDebtorInvoicesCurrent')
    number = EConomicsProperty('Number')


class Subscriber(EConomicsModel):
    __filters__ = [{'name': u'subscripton_list', 'method': u'FindBySubscriptonList'}, {'name': u'subscription', 'method': u'FindBySubscription'}]
    quantity_factor = EConomicsProperty('QuantityFactor')
    debtor = EConomicsReference('Debtor', 'Debtor')
    project = EConomicsReference('Project', 'Project')
    price_index = EConomicsProperty('PriceIndex')
    extra_text_for_invoice = EConomicsProperty('ExtraTextForInvoice')
    special_price = EConomicsProperty('SpecialPrice')
    start_date = EConomicsProperty('StartDate')
    expiry_date = EConomicsProperty('ExpiryDate')
    discount_as_percent = EConomicsProperty('DiscountAsPercent')
    discount_expiry_date = EConomicsProperty('DiscountExpiryDate')
    registered_date = EConomicsProperty('RegisteredDate')
    comments = EConomicsProperty('Comments')
    end_date = EConomicsProperty('EndDate')
    subscription = EConomicsReference('Subscription', 'Subscription')


class Department(EConomicsModel):
    __filters__ = [{'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class CreditorEntry(EConomicsModel):
    __filters__ = [{'name': u'invoice_number', 'method': u'FindByInvoiceNumber'}, {'name': u'serial_number', 'method': u'FindBySerialNumber'}, {'name': u'serial_number_type_and_invoice_number', 'method': u'FindBySerialNumberTypeAndInvoiceNumber'}]
    remainder_default_currency = EConomicsProperty('RemainderDefaultCurrency')
    date = EConomicsProperty('Date')
    amount = EConomicsProperty('Amount')
    voucher_number = EConomicsProperty('VoucherNumber')
    account = EConomicsReference('Account', 'Account')
    type = EConomicsProperty('Type')
    serial_number = EConomicsProperty('SerialNumber')
    remainder = EConomicsProperty('Remainder')
    invoice_number = EConomicsProperty('InvoiceNumber')
    currency = EConomicsReference('Currency', 'Currency')
    due_date = EConomicsProperty('DueDate')
    amount_default_currency = EConomicsProperty('AmountDefaultCurrency')
    text = EConomicsProperty('Text')
    creditor = EConomicsReference('Creditor', 'Creditor')


class AccountingYear(EConomicsModel):
    __filters__ = [{'name': u'date', 'method': u'FindByDate'}]
    is_closed = EConomicsProperty('IsClosed')
    periods = EConomicsProperty('Periods')
    year = EConomicsProperty('Year')
    from_date = EConomicsProperty('FromDate')
    to_date = EConomicsProperty('ToDate')


class ReportCode(EConomicsModel):
    __filters__ = []
    parent_code = EConomicsProperty('ParentCode')
    code = EConomicsProperty('Code')
    accounts = EConomicsReferenceList('Accounts', 'Account', 'ReportCode_GetAccounts')
    full_code = EConomicsProperty('FullCode')


class Employee(EConomicsModel):
    __filters__ = [{'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}]
    name = EConomicsProperty('Name')
    mileage_entries_by_date = EConomicsProperty('MileageEntriesByDate')
    cost_price = EConomicsProperty('CostPrice')
    group = EConomicsProperty('Group')
    sales_price = EConomicsProperty('SalesPrice')
    type = EConomicsProperty('Type')
    time_entries_by_date = EConomicsProperty('TimeEntriesByDate')
    time_entries = EConomicsReferenceList('TimeEntries', 'TimeEntry', 'Employee_GetTimeEntries')
    number = EConomicsProperty('Number')


class OrderLine(EConomicsModel):
    __filters__ = [{'name': u'product', 'method': u'FindByProduct'}, {'name': u'product_list', 'method': u'FindByProductList'}]
    quantity = EConomicsProperty('Quantity')
    discount_as_percent = EConomicsProperty('DiscountAsPercent')
    description = EConomicsProperty('Description')
    order = EConomicsReference('Order', 'Order')
    department = EConomicsReference('Department', 'Department')
    unit_net_price = EConomicsProperty('UnitNetPrice')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    unit = EConomicsReference('Unit', 'Unit')
    margin_as_percent = EConomicsProperty('MarginAsPercent')
    product = EConomicsReference('Product', 'Product')
    number = EConomicsProperty('Number')
    unit_cost_price = EConomicsProperty('UnitCostPrice')
    delivery_date = EConomicsProperty('DeliveryDate')
    total_net_amount = EConomicsProperty('TotalNetAmount')
    total_margin = EConomicsProperty('TotalMargin')


class EmployeeGroup(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'number_list', 'method': u'FindByNumberList'}]
    employees = EConomicsReferenceList('Employees', 'Employee', 'EmployeeGroup_GetEmployees')
    number = EConomicsProperty('Number')
    name = EConomicsProperty('Name')


class CurrentInvoice(EConomicsModel):
    __filters__ = [{'name': u'our_reference', 'method': u'FindByOurReference'}, {'name': u'other_reference', 'method': u'FindByOtherReference'}, {'name': u'date_interval', 'method': u'FindByDateInterval'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    delivery_location = EConomicsReference('DeliveryLocation', 'DeliveryLocation')
    delivery_country = EConomicsProperty('DeliveryCountry')
    is_vat_included = EConomicsProperty('IsVatIncluded')
    debtor_city = EConomicsProperty('DebtorCity')
    debtor_postal_code = EConomicsProperty('DebtorPostalCode')
    net_amount = EConomicsProperty('NetAmount')
    lines = EConomicsReferenceList('Lines', 'CurrentInvoiceLine', 'CurrentInvoice_GetLines')
    deduction_amount = EConomicsProperty('DeductionAmount')
    margin_as_percent = EConomicsProperty('MarginAsPercent')
    vat_amount = EConomicsProperty('VatAmount')
    currency = EConomicsReference('Currency', 'Currency')
    margin = EConomicsProperty('Margin')
    delivery_city = EConomicsProperty('DeliveryCity')
    date = EConomicsProperty('Date')
    debtor = EConomicsReference('Debtor', 'Debtor')
    delivery_county = EConomicsProperty('DeliveryCounty')
    other_reference = EConomicsProperty('OtherReference')
    debtor_county = EConomicsProperty('DebtorCounty')
    delivery_address = EConomicsProperty('DeliveryAddress')
    public_entry_number = EConomicsProperty('PublicEntryNumber')
    debtor_ean = EConomicsProperty('DebtorEan')
    pdf = EConomicsFileProperty('Pdf', 'CurrentInvoice_GetPdf', 'pdf')
    layout = EConomicsReference('Layout', 'TemplateCollection')
    terms_of_delivery = EConomicsProperty('TermsOfDelivery')
    due_date = EConomicsProperty('DueDate')
    our_reference2 = EConomicsReference('OurReference2', 'Employee')
    your_reference = EConomicsProperty('YourReference')
    our_reference = EConomicsReference('OurReference', 'Employee')
    gross_amount = EConomicsProperty('GrossAmount')
    exchange_rate = EConomicsProperty('ExchangeRate')
    delivery_date = EConomicsProperty('DeliveryDate')
    rounding_amount = EConomicsProperty('RoundingAmount')
    attention = EConomicsProperty('Attention')
    delivery_postal_code = EConomicsProperty('DeliveryPostalCode')
    heading = EConomicsProperty('Heading')
    debtor_name = EConomicsProperty('DebtorName')
    debtor_address = EConomicsProperty('DebtorAddress')
    project = EConomicsReference('Project', 'Project')
    debtor_country = EConomicsProperty('DebtorCountry')
    term_of_payment = EConomicsReference('TermOfPayment', 'TermOfPayment')
    text_line1 = EConomicsProperty('TextLine1')
    text_line2 = EConomicsProperty('TextLine2')


class CurrentSupplierInvoiceLine(EConomicsModel):
    __filters__ = []
    unit_price = EConomicsProperty('UnitPrice')
    product = EConomicsReference('Product', 'Product')
    quantity = EConomicsProperty('Quantity')
    invoice = EConomicsReference('Invoice', 'Invoice')


class Product(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'bar_code', 'method': u'FindByBarCode'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'all_accessible', 'method': u'GetAllAccessible'}]
    on_order = EConomicsProperty('OnOrder')
    description = EConomicsProperty('Description')
    sales_price = EConomicsProperty('SalesPrice')
    in_stock = EConomicsProperty('InStock')
    recommended_price = EConomicsProperty('RecommendedPrice')
    cost_price = EConomicsProperty('CostPrice')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    number = EConomicsProperty('Number')
    volume = EConomicsProperty('Volume')
    name = EConomicsProperty('Name')
    department = EConomicsReference('Department', 'Department')
    available = EConomicsProperty('Available')
    ordered = EConomicsReference('Ordered', 'Order')
    product_group = EConomicsReference('ProductGroup', 'ProductGroup')
    unit = EConomicsReference('Unit', 'Unit')
    is_accessible = EConomicsProperty('IsAccessible')
    bar_code = EConomicsProperty('BarCode')


class ProductPrice(EConomicsModel):
    __filters__ = [{'name': u'product_and_currency', 'method': u'FindByProductAndCurrency'}]
    product = EConomicsReference('Product', 'Product')
    currency = EConomicsReference('Currency', 'Currency')
    price = EConomicsProperty('Price')


class Currency(EConomicsModel):
    __filters__ = [{'name': u'code', 'method': u'FindByCode'}]
    code = EConomicsProperty('Code')


class Company(EConomicsModel):
    __filters__ = []
    number = EConomicsProperty('Number')
    fax_number = EConomicsProperty('FaxNumber')
    county = EConomicsProperty('County')
    country = EConomicsProperty('Country')
    base_currency = EConomicsProperty('BaseCurrency')
    address2 = EConomicsProperty('Address2')
    address1 = EConomicsProperty('Address1')
    ci_number = EConomicsProperty('CINumber')
    city = EConomicsProperty('City')
    web_site = EConomicsProperty('WebSite')
    contact = EConomicsProperty('Contact')
    email = EConomicsProperty('Email')
    telephone_number = EConomicsProperty('TelephoneNumber')
    mobile_number = EConomicsProperty('MobileNumber')
    postal_code = EConomicsProperty('PostalCode')
    name = EConomicsProperty('Name')
    vat_number = EConomicsProperty('VatNumber')
    sign_up_date = EConomicsProperty('SignUpDate')


class CashBookEntry(EConomicsModel):
    __filters__ = []
    currency = EConomicsReference('Currency', 'Currency')
    amount = EConomicsProperty('Amount')
    creditor_invoice_number = EConomicsProperty('CreditorInvoiceNumber')
    debtor = EConomicsReference('Debtor', 'Debtor')
    vat_account = EConomicsReference('VatAccount', 'VatAccount')
    cost_type = EConomicsReference('CostType', 'CostType')
    cash_book = EConomicsReference('CashBook', 'CashBook')
    bank_payment_type = EConomicsReference('BankPaymentType', 'BankPaymentType')
    project = EConomicsReference('Project', 'Project')
    debtor_invoice_number = EConomicsProperty('DebtorInvoiceNumber')
    creditor = EConomicsReference('Creditor', 'Creditor')
    bank_payment_creditor_invoice_id = EConomicsProperty('BankPaymentCreditorInvoiceId')
    voucher_number = EConomicsProperty('VoucherNumber')
    type = EConomicsProperty('Type')
    contra_account = EConomicsProperty('ContraAccount')
    employee = EConomicsReference('Employee', 'Employee')
    text = EConomicsProperty('Text')
    account = EConomicsReference('Account', 'Account')
    end_date = EConomicsProperty('EndDate')
    due_date = EConomicsProperty('DueDate')
    amount_default_currency = EConomicsProperty('AmountDefaultCurrency')
    start_date = EConomicsProperty('StartDate')
    contra_vat_account = EConomicsProperty('ContraVatAccount')
    bank_payment_creditor_id = EConomicsProperty('BankPaymentCreditorId')
    department = EConomicsReference('Department', 'Department')
    date = EConomicsProperty('Date')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    capitalise = EConomicsProperty('Capitalise')


class Order(EConomicsModel):
    __filters__ = [{'name': u'all_current', 'method': u'GetAllCurrent'}, {'name': u'other_reference', 'method': u'FindByOtherReference'}, {'name': u'number_interval', 'method': u'FindByNumberInterval'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'date_interval', 'method': u'FindByDateInterval'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    other_reference = EConomicsProperty('OtherReference')
    gross_amount = EConomicsProperty('GrossAmount')
    public_entry_number = EConomicsProperty('PublicEntryNumber')
    net_amount = EConomicsProperty('NetAmount')
    margin_as_percent = EConomicsProperty('MarginAsPercent')
    debtor_county = EConomicsProperty('DebtorCounty')
    delivery_county = EConomicsProperty('DeliveryCounty')
    is_vat_included = EConomicsProperty('IsVatIncluded')
    lines = EConomicsReferenceList('Lines', 'OrderLine', 'Order_GetLines')
    project = EConomicsReference('Project', 'Project')
    pdf = EConomicsFileProperty('Pdf', 'Order_GetPdf', 'pdf')
    due_date = EConomicsProperty('DueDate')
    rounding_amount = EConomicsProperty('RoundingAmount')
    terms_of_delivery = EConomicsProperty('TermsOfDelivery')
    debtor_ean = EConomicsProperty('DebtorEan')
    layout = EConomicsReference('Layout', 'TemplateCollection')
    debtor_city = EConomicsProperty('DebtorCity')
    term_of_payment = EConomicsReference('TermOfPayment', 'TermOfPayment')
    vat_amount = EConomicsProperty('VatAmount')
    debtor_name = EConomicsProperty('DebtorName')
    debtor_country = EConomicsProperty('DebtorCountry')
    is_sent = EConomicsProperty('IsSent')
    debtor = EConomicsReference('Debtor', 'Debtor')
    delivery_date = EConomicsProperty('DeliveryDate')
    our_reference = EConomicsReference('OurReference', 'Employee')
    debtor_postal_code = EConomicsProperty('DebtorPostalCode')
    our_reference2 = EConomicsReference('OurReference2', 'Employee')
    debtor_address = EConomicsProperty('DebtorAddress')
    margin = EConomicsProperty('Margin')
    exchange_rate = EConomicsProperty('ExchangeRate')
    date = EConomicsProperty('Date')
    delivery_country = EConomicsProperty('DeliveryCountry')
    number = EConomicsProperty('Number')
    your_reference = EConomicsProperty('YourReference')
    text_line1 = EConomicsProperty('TextLine1')
    text_line2 = EConomicsProperty('TextLine2')
    delivery_address = EConomicsProperty('DeliveryAddress')
    is_archived = EConomicsProperty('IsArchived')
    delivery_city = EConomicsProperty('DeliveryCity')
    heading = EConomicsProperty('Heading')
    delivery_postal_code = EConomicsProperty('DeliveryPostalCode')
    delivery_location = EConomicsReference('DeliveryLocation', 'DeliveryLocation')
    attention = EConomicsProperty('Attention')
    currency = EConomicsReference('Currency', 'Currency')


class CurrentSupplierInvoice(EConomicsModel):
    __filters__ = []
    id = EConomicsProperty('Id')
    lines = EConomicsProperty('Lines')
    creditor = EConomicsReference('Creditor', 'Creditor')


class BankPaymentType(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'number_list', 'method': u'FindByNumberList'}]
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class DebtorGroup(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'number_list', 'method': u'FindByNumberList'}]
    name = EConomicsProperty('Name')
    account = EConomicsReference('Account', 'Account')
    debtors = EConomicsReferenceList('Debtors', 'Debtor', 'DebtorGroup_GetDebtors')
    layout = EConomicsReference('Layout', 'TemplateCollection')
    number = EConomicsProperty('Number')


class InvoiceLine(EConomicsModel):
    __filters__ = [{'name': u'invoice_number_interval', 'method': u'FindByInvoiceNumberInterval'}, {'name': u'product', 'method': u'FindByProduct'}, {'name': u'product_list', 'method': u'FindByProductList'}]
    product = EConomicsReference('Product', 'Product')
    number = EConomicsProperty('Number')
    discount_as_percent = EConomicsProperty('DiscountAsPercent')
    department = EConomicsReference('Department', 'Department')
    invoice = EConomicsReference('Invoice', 'Invoice')
    unit = EConomicsReference('Unit', 'Unit')
    quantity = EConomicsProperty('Quantity')
    vat_amount = EConomicsProperty('VatAmount')
    total_net_amount = EConomicsProperty('TotalNetAmount')
    description = EConomicsProperty('Description')
    vat_rate = EConomicsProperty('VatRate')
    delivery_date = EConomicsProperty('DeliveryDate')
    unit_cost_price = EConomicsProperty('UnitCostPrice')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    unit_net_price = EConomicsProperty('UnitNetPrice')


class Quotation(EConomicsModel):
    __filters__ = [{'name': u'date_interval', 'method': u'FindByDateInterval'}, {'name': u'other_reference', 'method': u'FindByOtherReference'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_current', 'method': u'GetAllCurrent'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'number_interval', 'method': u'FindByNumberInterval'}]
    debtor_address = EConomicsProperty('DebtorAddress')
    is_vat_included = EConomicsProperty('IsVatIncluded')
    public_entry_number = EConomicsProperty('PublicEntryNumber')
    date = EConomicsProperty('Date')
    currency = EConomicsReference('Currency', 'Currency')
    debtor_city = EConomicsProperty('DebtorCity')
    debtor_country = EConomicsProperty('DebtorCountry')
    due_date = EConomicsProperty('DueDate')
    debtor = EConomicsReference('Debtor', 'Debtor')
    margin = EConomicsProperty('Margin')
    other_reference = EConomicsProperty('OtherReference')
    our_reference = EConomicsReference('OurReference', 'Employee')
    delivery_address = EConomicsProperty('DeliveryAddress')
    your_reference = EConomicsProperty('YourReference')
    heading = EConomicsProperty('Heading')
    text_line2 = EConomicsProperty('TextLine2')
    text_line1 = EConomicsProperty('TextLine1')
    gross_amount = EConomicsProperty('GrossAmount')
    margin_as_percent = EConomicsProperty('MarginAsPercent')
    delivery_county = EConomicsProperty('DeliveryCounty')
    is_sent = EConomicsProperty('IsSent')
    delivery_date = EConomicsProperty('DeliveryDate')
    delivery_postal_code = EConomicsProperty('DeliveryPostalCode')
    terms_of_delivery = EConomicsProperty('TermsOfDelivery')
    our_reference2 = EConomicsReference('OurReference2', 'Employee')
    term_of_payment = EConomicsReference('TermOfPayment', 'TermOfPayment')
    debtor_name = EConomicsProperty('DebtorName')
    lines = EConomicsReferenceList('Lines', 'QuotationLine', 'Quotation_GetLines')
    delivery_location = EConomicsReference('DeliveryLocation', 'DeliveryLocation')
    layout = EConomicsReference('Layout', 'TemplateCollection')
    attention = EConomicsProperty('Attention')
    is_archived = EConomicsProperty('IsArchived')
    debtor_postal_code = EConomicsProperty('DebtorPostalCode')
    rounding_amount = EConomicsProperty('RoundingAmount')
    net_amount = EConomicsProperty('NetAmount')
    vat_amount = EConomicsProperty('VatAmount')
    debtor_county = EConomicsProperty('DebtorCounty')
    pdf = EConomicsProperty('Pdf')
    number = EConomicsProperty('Number')
    debtor_ean = EConomicsProperty('DebtorEan')
    delivery_city = EConomicsProperty('DeliveryCity')
    exchange_rate = EConomicsProperty('ExchangeRate')
    delivery_country = EConomicsProperty('DeliveryCountry')


class Debtor(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'ci_number', 'method': u'FindByCINumber'}, {'name': u'partial_name', 'method': u'FindByPartialName'}, {'name': u'telephone_and_fax_number', 'method': u'FindByTelephoneAndFaxNumber'}, {'name': u'ean', 'method': u'FindByEan'}, {'name': u'email', 'method': u'FindByEmail'}, {'name': u'number', 'method': u'FindByNumber'}]
    attention = EConomicsProperty('Attention')
    number = EConomicsProperty('Number')
    address = EConomicsProperty('Address')
    postal_code = EConomicsProperty('PostalCode')
    website = EConomicsProperty('Website')
    telephone_and_fax_number = EConomicsProperty('TelephoneAndFaxNumber')
    city = EConomicsProperty('City')
    your_reference = EConomicsProperty('YourReference')
    country = EConomicsProperty('Country')
    invoices = EConomicsReferenceList('Invoices', 'Invoice', 'Debtor_GetInvoices')
    extended_vat_zone = EConomicsReference('ExtendedVatZone', 'ExtendedVatZone')
    is_accessible = EConomicsProperty('IsAccessible')
    email = EConomicsProperty('Email')
    balance = EConomicsProperty('Balance')
    layout = EConomicsReference('Layout', 'TemplateCollection')
    vat_zone = EConomicsProperty('VatZone')
    debtor_contacts = EConomicsReferenceList('DebtorContacts', 'DebtorContact', 'Debtor_GetDebtorContacts')
    term_of_payment = EConomicsReference('TermOfPayment', 'TermOfPayment')
    quotations = EConomicsReferenceList('Quotations', 'Quotation', 'Debtor_GetQuotations')
    price_group = EConomicsReference('PriceGroup', 'PriceGroup')
    ean = EConomicsProperty('Ean')
    name = EConomicsProperty('Name')
    our_reference = EConomicsReference('OurReference', 'Employee')
    county = EConomicsProperty('County')
    ci_number = EConomicsProperty('CINumber')
    orders = EConomicsReferenceList('Orders', 'Order', 'Debtor_GetOrders')
    public_entry_number = EConomicsProperty('PublicEntryNumber')
    delivery_locations = EConomicsReferenceList('DeliveryLocations', 'DeliveryLocation', 'Debtor_GetDeliveryLocations')
    currency = EConomicsReference('Currency', 'Currency')
    current_invoices = EConomicsReferenceList('CurrentInvoices', 'CurrentInvoice', 'Debtor_GetCurrentInvoices')
    next_available_number = EConomicsProperty('NextAvailableNumber')
    vat_number = EConomicsProperty('VatNumber')
    debtor_group = EConomicsReference('DebtorGroup', 'DebtorGroup')
    credit_maximum = EConomicsProperty('CreditMaximum')
    entries = EConomicsReferenceList('Entries', 'Entry', 'Debtor_GetEntries')
    open_entries = EConomicsProperty('OpenEntries')
    subscribers = EConomicsReferenceList('Subscribers', 'Subscriber', 'Debtor_GetSubscribers')


class CreditorGroup(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'number', 'method': u'FindByNumber'}]
    creditors = EConomicsReferenceList('Creditors', 'Creditor', 'CreditorGroup_GetCreditors')
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')
    account = EConomicsReference('Account', 'Account')


class KeyFigureCode(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}]
    accounts = EConomicsReferenceList('Accounts', 'Account', 'KeyFigureCode_GetAccounts')
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class MileageEntry(EConomicsModel):
    __filters__ = []
    start_location = EConomicsProperty('StartLocation')
    id = EConomicsProperty('Id')
    end_location = EConomicsProperty('EndLocation')
    date = EConomicsProperty('Date')
    cost_rate = EConomicsProperty('CostRate')
    approved = EConomicsProperty('Approved')
    distance = EConomicsProperty('Distance')
    employee = EConomicsReference('Employee', 'Employee')
    sales_rate = EConomicsProperty('SalesRate')
    project = EConomicsReference('Project', 'Project')


class Project(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'number_list', 'method': u'FindByNumberList'}]
    debtor = EConomicsReference('Debtor', 'Debtor')
    entries = EConomicsReferenceList('Entries', 'Entry', 'Project_GetEntries')
    open_sub_projects = EConomicsProperty('OpenSubProjects')
    time_entries_by_date = EConomicsProperty('TimeEntriesByDate')
    project_group = EConomicsReference('ProjectGroup', 'ProjectGroup')
    is_main_project = EConomicsProperty('IsMainProject')
    entries_by_date = EConomicsProperty('EntriesByDate')
    description = EConomicsProperty('Description')
    is_closed = EConomicsProperty('IsClosed')
    name = EConomicsProperty('Name')
    main_project = EConomicsProperty('MainProject')
    activities = EConomicsReferenceList('Activities', 'Activity', 'Project_GetActivities')
    is_accessible = EConomicsProperty('IsAccessible')
    mileage_entries_by_date = EConomicsProperty('MileageEntriesByDate')
    time_entries = EConomicsReferenceList('TimeEntries', 'TimeEntry', 'Project_GetTimeEntries')
    number = EConomicsProperty('Number')
    responsible = EConomicsProperty('Responsible')
    mileage = EConomicsProperty('Mileage')


class Account(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    is_accessible = EConomicsProperty('IsAccessible')
    name = EConomicsProperty('Name')
    department = EConomicsReference('Department', 'Department')
    block_direct_entries = EConomicsProperty('BlockDirectEntries')
    sum_intervals = EConomicsReferenceList('SumIntervals', 'SumInterval', 'Account_GetSumIntervals')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    budget_figures_by_date = EConomicsProperty('BudgetFiguresByDate')
    balance = EConomicsProperty('Balance')
    budget_figures = EConomicsReferenceList('BudgetFigures', 'BudgetFigure', 'Account_GetBudgetFigures')
    type = EConomicsProperty('Type')
    number = EConomicsProperty('Number')
    vat_account = EConomicsReference('VatAccount', 'VatAccount')
    contra_account = EConomicsProperty('ContraAccount')
    entries_by_date = EConomicsProperty('EntriesByDate')
    opening_account = EConomicsProperty('OpeningAccount')
    entry_totals_by_date = EConomicsProperty('EntryTotalsByDate')
    debit_credit = EConomicsProperty('DebitCredit')
    entries_by_number = EConomicsProperty('EntriesByNumber')
    total_from = EConomicsProperty('TotalFrom')


class Activity(EConomicsModel):
    __filters__ = [{'name': u'number', 'method': u'FindByNumber'}, {'name': u'number_list', 'method': u'FindByNumberList'}]
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class Entry(EConomicsModel):
    __filters__ = [{'name': u'date_interval', 'method': u'FindByDateInterval'}, {'name': u'serial_number_interval', 'method': u'FindBySerialNumberInterval'}]
    account = EConomicsReference('Account', 'Account')
    project = EConomicsReference('Project', 'Project')
    currency = EConomicsReference('Currency', 'Currency')
    vat_account = EConomicsReference('VatAccount', 'VatAccount')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    amount_default_currency = EConomicsProperty('AmountDefaultCurrency')
    document = EConomicsProperty('Document')
    department = EConomicsReference('Department', 'Department')
    voucher_number = EConomicsProperty('VoucherNumber')
    last_used_serial_number = EConomicsProperty('LastUsedSerialNumber')
    type = EConomicsProperty('Type')
    text = EConomicsProperty('Text')
    amount = EConomicsProperty('Amount')
    serial_number = EConomicsProperty('SerialNumber')
    date = EConomicsProperty('Date')


class CurrentInvoiceLine(EConomicsModel):
    __filters__ = [{'name': u'product_list', 'method': u'FindByProductList'}, {'name': u'product', 'method': u'FindByProduct'}]
    total_net_amount = EConomicsProperty('TotalNetAmount')
    quantity = EConomicsProperty('Quantity')
    product = EConomicsReference('Product', 'Product')
    description = EConomicsProperty('Description')
    department = EConomicsReference('Department', 'Department')
    discount_as_percent = EConomicsProperty('DiscountAsPercent')
    unit_cost_price = EConomicsProperty('UnitCostPrice')
    margin_as_percent = EConomicsProperty('MarginAsPercent')
    unit_net_price = EConomicsProperty('UnitNetPrice')
    unit = EConomicsReference('Unit', 'Unit')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    invoice = EConomicsReference('Invoice', 'Invoice')
    delivery_date = EConomicsProperty('DeliveryDate')
    total_margin = EConomicsProperty('TotalMargin')
    number = EConomicsProperty('Number')


class SumInterval(EConomicsModel):
    __filters__ = []
    to_account = EConomicsProperty('ToAccount')
    from_account = EConomicsProperty('FromAccount')
    account = EConomicsReference('Account', 'Account')


class TermOfPayment(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}]
    debtor = EConomicsReference('Debtor', 'Debtor')
    distribution_in_percent2 = EConomicsProperty('DistributionInPercent2')
    contra_account2 = EConomicsProperty('ContraAccount2')
    name = EConomicsProperty('Name')
    days = EConomicsProperty('Days')
    distribution_in_percent = EConomicsProperty('DistributionInPercent')
    type = EConomicsProperty('Type')
    contra_account = EConomicsProperty('ContraAccount')
    description = EConomicsProperty('Description')


class TimeEntry(EConomicsModel):
    __filters__ = [{'name': u'all_updated', 'method': u'GetAllUpdated'}, {'name': u'all_updated', 'method': u'GetAllUpdated'}]
    text = EConomicsProperty('Text')
    approved = EConomicsProperty('Approved')
    date = EConomicsProperty('Date')
    project = EConomicsReference('Project', 'Project')
    number_of_hours = EConomicsProperty('NumberOfHours')
    employee = EConomicsReference('Employee', 'Employee')
    id = EConomicsProperty('Id')
    activity = EConomicsReference('Activity', 'Activity')


class PriceGroup(EConomicsModel):
    __filters__ = [{'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'name', 'method': u'FindByName'}]
    price = EConomicsProperty('Price')
    number = EConomicsProperty('Number')
    name = EConomicsProperty('Name')


class CreditorContact(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}]
    creditor = EConomicsReference('Creditor', 'Creditor')
    telephone_number = EConomicsProperty('TelephoneNumber')
    external_id = EConomicsProperty('ExternalId')
    comments = EConomicsProperty('Comments')
    email = EConomicsProperty('Email')
    number = EConomicsProperty('Number')
    name = EConomicsProperty('Name')


class DocumentArchiveCategory(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}]
    documents = EConomicsProperty('Documents')
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class VatAccount(EConomicsModel):
    __filters__ = [{'name': u'vat_code', 'method': u'FindByVatCode'}]
    rate_as_percent = EConomicsProperty('RateAsPercent')
    contra_account = EConomicsProperty('ContraAccount')
    type = EConomicsProperty('Type')
    account = EConomicsReference('Account', 'Account')
    name = EConomicsProperty('Name')
    vat_code = EConomicsProperty('VatCode')


class QuotationLine(EConomicsModel):
    __filters__ = [{'name': u'product_list', 'method': u'FindByProductList'}, {'name': u'product', 'method': u'FindByProduct'}]
    department = EConomicsReference('Department', 'Department')
    total_margin = EConomicsProperty('TotalMargin')
    number = EConomicsProperty('Number')
    total_net_amount = EConomicsProperty('TotalNetAmount')
    unit_net_price = EConomicsProperty('UnitNetPrice')
    margin_as_percent = EConomicsProperty('MarginAsPercent')
    description = EConomicsProperty('Description')
    discount_as_percent = EConomicsProperty('DiscountAsPercent')
    distribution_key = EConomicsReference('DistributionKey', 'DistributionKey')
    delivery_date = EConomicsProperty('DeliveryDate')
    quantity = EConomicsProperty('Quantity')
    unit = EConomicsReference('Unit', 'Unit')
    quotation = EConomicsReference('Quotation', 'Quotation')
    unit_cost_price = EConomicsProperty('UnitCostPrice')
    product = EConomicsReference('Product', 'Product')


class ScannedDocument(EConomicsModel):
    __filters__ = [{'name': u'voucher_number', 'method': u'FindByVoucherNumber'}, {'name': u'voucher_number_interval', 'method': u'FindByVoucherNumberInterval'}]
    to_date = EConomicsProperty('ToDate')
    from_date = EConomicsProperty('FromDate')
    page_count = EConomicsProperty('PageCount')
    status = EConomicsProperty('Status')
    number = EConomicsProperty('Number')
    voucher_number = EConomicsProperty('VoucherNumber')
    pdf = EConomicsProperty('Pdf')
    category = EConomicsProperty('Category')
    note = EConomicsProperty('Note')


class SubscriptionLine(EConomicsModel):
    __filters__ = [{'name': u'product_list', 'method': u'FindByProductList'}, {'name': u'subscripton_list', 'method': u'FindBySubscriptonList'}, {'name': u'product', 'method': u'FindByProduct'}, {'name': u'subscription', 'method': u'FindBySubscription'}]
    department = EConomicsReference('Department', 'Department')
    quantity = EConomicsProperty('Quantity')
    subscription = EConomicsReference('Subscription', 'Subscription')
    number = EConomicsProperty('Number')
    product = EConomicsReference('Product', 'Product')
    special_price = EConomicsProperty('SpecialPrice')
    product_name = EConomicsProperty('ProductName')


class DeliveryLocation(EConomicsModel):
    __filters__ = [{'name': u'external_id', 'method': u'FindByExternalId'}]
    address = EConomicsProperty('Address')
    postal_code = EConomicsProperty('PostalCode')
    terms_of_delivery = EConomicsProperty('TermsOfDelivery')
    debtor = EConomicsReference('Debtor', 'Debtor')
    country = EConomicsProperty('Country')
    city = EConomicsProperty('City')
    number = EConomicsProperty('Number')
    county = EConomicsProperty('County')
    is_accessible = EConomicsProperty('IsAccessible')
    external_id = EConomicsProperty('ExternalId')


class Invoice(EConomicsModel):
    __filters__ = [{'name': u'date_interval', 'method': u'FindByDateInterval'}, {'name': u'number_interval', 'method': u'FindByNumberInterval'}, {'name': u'our_reference', 'method': u'FindByOurReference'}, {'name': u'number', 'method': u'FindByNumber'}, {'name': u'order_number', 'method': u'FindByOrderNumber'}, {'name': u'other_reference', 'method': u'FindByOtherReference'}, {'name': u'number_list', 'method': u'FindByNumberList'}]
    vat_amount = EConomicsProperty('VatAmount')
    other_reference = EConomicsProperty('OtherReference')
    oio_xml = EConomicsProperty('OioXml')
    debtor_ean = EConomicsProperty('DebtorEan')
    debtor_postal_code = EConomicsProperty('DebtorPostalCode')
    terms_of_delivery = EConomicsProperty('TermsOfDelivery')
    remainder = EConomicsProperty('Remainder')
    delivery_county = EConomicsProperty('DeliveryCounty')
    our_reference = EConomicsReference('OurReference', 'Employee')
    currency = EConomicsReference('Currency', 'Currency')
    debtor_name = EConomicsProperty('DebtorName')
    date = EConomicsProperty('Date')
    net_amount = EConomicsProperty('NetAmount')
    number = EConomicsProperty('Number')
    remainder_default_currency = EConomicsProperty('RemainderDefaultCurrency')
    order_number = EConomicsProperty('OrderNumber')
    term_of_payment = EConomicsReference('TermOfPayment', 'TermOfPayment')
    delivery_postal_code = EConomicsProperty('DeliveryPostalCode')
    debtor_address = EConomicsProperty('DebtorAddress')
    project = EConomicsReference('Project', 'Project')
    attention = EConomicsProperty('Attention')
    is_vat_included = EConomicsProperty('IsVatIncluded')
    due_date = EConomicsProperty('DueDate')
    our_reference2 = EConomicsReference('OurReference2', 'Employee')
    delivery_date = EConomicsProperty('DeliveryDate')
    public_entry_number = EConomicsProperty('PublicEntryNumber')
    debtor_city = EConomicsProperty('DebtorCity')
    layout = EConomicsReference('Layout', 'TemplateCollection')
    text_line1 = EConomicsProperty('TextLine1')
    text_line2 = EConomicsProperty('TextLine2')
    rounding_amount = EConomicsProperty('RoundingAmount')
    pdf = EConomicsFileProperty('Pdf', 'Invoice_GetPdf', 'pdf')
    debtor_country = EConomicsProperty('DebtorCountry')
    delivery_location = EConomicsReference('DeliveryLocation', 'DeliveryLocation')
    heading = EConomicsProperty('Heading')
    delivery_city = EConomicsProperty('DeliveryCity')
    debtor = EConomicsReference('Debtor', 'Debtor')
    gross_amount = EConomicsProperty('GrossAmount')
    lines = EConomicsReferenceList('Lines', 'InvoiceLine', 'Invoice_GetLines')
    your_reference = EConomicsProperty('YourReference')
    deduction_amount = EConomicsProperty('DeductionAmount')
    net_amount_default_currency = EConomicsProperty('NetAmountDefaultCurrency')
    debtor_county = EConomicsProperty('DebtorCounty')
    delivery_country = EConomicsProperty('DeliveryCountry')
    delivery_address = EConomicsProperty('DeliveryAddress')


class DebtorContact(EConomicsModel):
    __filters__ = [{'name': u'external_id', 'method': u'FindByExternalId'}, {'name': u'name', 'method': u'FindByName'}]
    is_to_receive_email_copy_of_order = EConomicsProperty('IsToReceiveEmailCopyOfOrder')
    comments = EConomicsProperty('Comments')
    debtor = EConomicsReference('Debtor', 'Debtor')
    number = EConomicsProperty('Number')
    email = EConomicsProperty('Email')
    name = EConomicsProperty('Name')
    is_to_receive_email_copy_of_invoice = EConomicsProperty('IsToReceiveEmailCopyOfInvoice')
    telephone_number = EConomicsProperty('TelephoneNumber')
    external_id = EConomicsProperty('ExternalId')


class ProjectGroup(EConomicsModel):
    __filters__ = [{'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}]
    projects = EConomicsReferenceList('Projects', 'Project', 'ProjectGroup_GetProjects')
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')


class Subscription(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}]
    number = EConomicsProperty('Number')
    description = EConomicsProperty('Description')
    collection = EConomicsProperty('Collection')
    calendar_year_basis = EConomicsProperty('CalendarYearBasis')
    include_name = EConomicsProperty('IncludeName')
    subscribers = EConomicsReferenceList('Subscribers', 'Subscriber', 'Subscription_GetSubscribers')
    next_available_number = EConomicsProperty('NextAvailableNumber')
    subscription_interval = EConomicsProperty('SubscriptionInterval')
    subscription_lines = EConomicsReferenceList('SubscriptionLines', 'SubscriptionLine', 'Subscription_GetSubscriptionLines')
    allow_more_than_one_for_each_debtor = EConomicsProperty('AllowMoreThanOneForEachDebtor')
    add_period = EConomicsProperty('AddPeriod')
    name = EConomicsProperty('Name')


class CashBook(EConomicsModel):
    __filters__ = [{'name': u'name', 'method': u'FindByName'}, {'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'name_list', 'method': u'FindByNameList'}, {'name': u'number', 'method': u'FindByNumber'}]
    number = EConomicsProperty('Number')
    entries = EConomicsReferenceList('Entries', 'Entry', 'CashBook_GetEntries')
    next_voucher_number = EConomicsProperty('NextVoucherNumber')
    name = EConomicsProperty('Name')


class Unit(EConomicsModel):
    __filters__ = [{'name': u'number_list', 'method': u'FindByNumberList'}, {'name': u'name', 'method': u'FindByName'}, {'name': u'number', 'method': u'FindByNumber'}]
    name = EConomicsProperty('Name')
    number = EConomicsProperty('Number')