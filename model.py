from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orders(db.Model):
    __table__name = 'orders'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    state = db.Column(db.String(50), nullable=True)
    billing_first_name = db.Column(db.String(50), nullable=True)
    billing_last_name = db.Column(db.String(50), nullable=True)
    date_created = db.Column(db.DateTime, nullable=True)
    date_modified = db.Column(db.DateTime, nullable=True)
    total = db.Column(db.Integer, nullable=True)
    total_tax = db.Column(db.Integer, nullable=True)
    currency = db.Column(db.String(11), nullable=True)
    version = db.Column(db.String(11), nullable=True)
    customer_id = db.Column(db.Integer)
    order_key = db.Column(db.String(100), nullable=True)
    payment_method = db.Column(db.String(50), nullable=True)
    payment_method_title = db.Column(db.String(50), nullable=True)
    transaction_id = db.Column(db.String(50), nullable=True)
    customer_ip_address = db.Column(db.String(50), nullable=True)
    created_via = db.Column(db.String(50), nullable=True)
    customer_id = db.Column(db.Integer, nullable=True)
    customer_note = db.Column(db.String(50), nullable=True)
    date_completed = db.Column(db.String(50), nullable=True)
    date_paid = db.Column(db.String(50), nullable=True)
    cart_hash = db.Column(db.String(50), nullable=True)
    billing_company = db.Column(db.String(50), nullable=True)
    billing_address_1 = db.Column(db.String(500), nullable=True)
    billing_address_2 = db.Column(db.String(500), nullable=True)
    billing_city = db.Column(db.String(50), nullable=True)
    billing_state = db.Column(db.String(50), nullable=True)
    billing_postcode = db.Column(db.String(50), nullable=True)
    billing_country = db.Column(db.String(50), nullable=True)
    billing_email = db.Column(db.String(50), nullable=True)
    billing_phone = db.Column(db.String(50), nullable=True)
    shipping_first_name = db.Column(db.String(50), nullable=True)
    shipping_last_name = db.Column(db.String(50), nullable=True)
    shipping_company = db.Column(db.String(50), nullable=True)
    shipping_address_1 = db.Column(db.String(500), nullable=True)
    shipping_address_2 = db.Column(db.String(500), nullable=True)
    shipping_city = db.Column(db.String(50), nullable=True)
    # shipping_state = shipping['state']
    shipping_postcode = db.Column(db.String(50), nullable=True)
    shipping_country = db.Column(db.String(50), nullable=True)

    def __init__(self, order_id, parent_id, state, billing_first_name, billing_last_name, currency, version, total,
                 total_tax, billing_company, billing_address_1, billing_address_2, billing_city, billing_state,
                 billing_postcode, billing_country, billing_email, billing_phone, shipping_first_name,
                 shipping_last_name, shipping_company, shipping_address_1, shipping_address_2, shipping_city,
                 shipping_postcode, shipping_country, payment_method, payment_method_title, transaction_id,
                 customer_ip_address, created_via, customer_id, customer_note, cart_hash):
        self.order_id = order_id
        self.parent_id = parent_id
        self.state = state
        self.billing_first_name = billing_first_name
        self.billing_last_name = billing_last_name
        self.currency = currency
        self.version = version
        self.total = total
        self.total_tax = total_tax
        self.date_created = datetime.utcnow()
        self.date_modified = datetime.utcnow()
        self.billing_company = billing_company
        self.billing_address_1 = billing_address_1
        self.billing_address_2 = billing_address_2
        self.billing_city = billing_city
        self.billing_state = billing_state
        self.billing_postcode = billing_postcode
        self.billing_country = billing_country
        self.billing_email = billing_email
        self.billing_phone = billing_phone
        self.shipping_first_name = shipping_first_name
        self.shipping_last_name = shipping_last_name
        self.shipping_company = shipping_company
        self.shipping_address_1 = shipping_address_1
        self.shipping_address_2 = shipping_address_2
        self.shipping_city = shipping_city
        self.shipping_postcode = shipping_postcode
        self.shipping_country = shipping_country
        self.payment_method = payment_method
        self.payment_method_title = payment_method_title
        self.transaction_id = transaction_id
        self.customer_ip_address = customer_ip_address
        self.created_via = created_via
        self.customer_id = customer_id
        self.customer_note = customer_note
        self.cart_hash = cart_hash


class OrdersLineItems(db.Model):
    __table__name = 'orders_line_items'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    line_items_id = db.Column(db.Integer)
    line_items_name = db.Column(db.String(100), nullable=True)
    line_items_product_id = db.Column(db.Integer)
    line_items_variation_id = db.Column(db.Integer)
    line_items_quantity = db.Column(db.Integer)
    line_items_tax_class = db.Column(db.String(100), nullable=True)
    line_items_subtotal = db.Column(db.Numeric(10, 6))
    line_items_subtotal_tax = db.Column(db.Numeric(10, 6))
    line_items_total = db.Column(db.Numeric(10, 6))
    line_items_total_tax = db.Column(db.Numeric(10, 6))
    line_items_taxes = db.Column(db.String(100), nullable=True)
    line_items_sku = db.Column(db.String(50), nullable=True)
    line_items_price = db.Column(db.Numeric(10, 6))
    line_items_parent_name = db.Column(db.String(100), nullable=True)

    def __init__(self, order_id, line_items_id, line_items_name, line_items_product_id,
                 line_items_variation_id, line_items_quantity, line_items_tax_class, line_items_subtotal,
                 line_items_subtotal_tax, line_items_total, line_items_total_tax, line_items_sku, line_items_price,
                 line_items_parent_name):
        self.order_id = order_id
        self.line_items_id = line_items_id
        self.line_items_name = line_items_name
        self.line_items_product_id = line_items_product_id
        self.line_items_variation_id = line_items_variation_id
        self.line_items_quantity = line_items_quantity
        self.line_items_tax_class = line_items_tax_class
        self.line_items_subtotal = line_items_subtotal
        self.line_items_subtotal_tax = line_items_subtotal_tax
        self.line_items_total = line_items_total
        self.line_items_total_tax = line_items_total_tax
        # self.line_items_taxes = line_items_taxes
        self.line_items_sku = line_items_sku
        self.line_items_price = line_items_price
        self.line_items_parent_name = line_items_parent_name
