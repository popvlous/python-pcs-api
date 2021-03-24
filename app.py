from datetime import datetime

from flask import Flask, jsonify, request, make_response, render_template
from sqlalchemy.cprocessors import str_to_date
from woocommerce import API
import json
from pymongo import MongoClient
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import insert

pymysql.install_as_MySQLdb()
from bson.objectid import ObjectId

# conn = MongoClient("mongodb://sds:Foxconn890@192.168.100.11:15017,192.168.100.12:15017,192.168.100.13:15017/sds")
# # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
# db = conn.sds
# collection = db.users
# collection1 = db.inspections

db = SQLAlchemy()

# woocommerce api
wcapi = API(
    url="https://store.pyrarc.com",
    consumer_key="ck_ab98c184df28b6bc3298710a139177b00564a302",
    consumer_secret="cs_9de359730bb8aa8d4faf3395541c503e90997294",
    version="wc/v3"
)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://pcs:Foxconn@890@192.168.100.14:3309/pcs"

db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/pcs/api/v1/product', methods=['POST'])
def show():
    productlist = wcapi.get("products", params={"per_page": 20}).json()
    return jsonify({
        'success': True,
        'msg': 'product list is {} '.format(productlist)
    })


@app.route('/pcs/api/v1/bc', methods=['POST'])
def order_details():
    request_data = request.data.decode('utf-8')
    j_request_data = json.loads(request_data)
    req_id = j_request_data['id']
    orderid = 'orders/' + str(req_id)
    order_details = wcapi.get(orderid).json()
    order_details_id = order_details['id']
    order_details_parent_id = order_details['parent_id']
    order_details_status = order_details['status']
    order_details_currency = order_details['currency']
    order_details_date_created = order_details['date_created']
    order_details_date_modified = order_details['date_modified']
    order_details_total = order_details['total']
    order_details_total_tax = order_details['total_tax']
    order_details_payment_method = order_details['payment_method']
    order_details_payment_method_title = order_details['payment_method_title']
    order_details_transaction_id = order_details['transaction_id']
    order_details_customer_ip_address = order_details['customer_ip_address']
    order_details_created_via = order_details['created_via']
    order_details_customer_note = order_details['customer_note']
    order_details_cart_hash = order_details['cart_hash']

    # 保存billing訊息
    billing = order_details['billing']
    billing_first_name = billing['first_name']
    billing_last_name = billing['last_name']
    billing_company = billing['company']
    billing_address_1 = billing['address_1']
    billing_address_2 = billing['address_2']
    billing_city = billing['city']
    billing_state = billing['state']
    billing_postcode = billing['postcode']
    billing_country = billing['country']
    billing_email = billing['email']
    billing_phone = billing['phone']
    # 保存shipping訊息
    shipping = order_details['shipping']
    shipping_first_name = shipping['first_name']
    shipping_last_name = shipping['last_name']
    shipping_company = shipping['company']
    shipping_address_1 = shipping['address_1']
    shipping_address_2 = shipping['address_2']
    shipping_city = shipping['city']
    #shipping_state = shipping['state']
    shipping_postcode = shipping['postcode']
    shipping_country = shipping['country']

    # sql = "INSERT INTO Orders (order_id, parent_id, status, billing_first_name, billing_last_name)VALUES (" + str(
    #     order_details_id) + ", " + "" + str(order_details_parent_id) + ", " + str(order_details_status) + ", " + str(
    #     billing_first_name) + ", " + str(billing_last_name) + ")"
    sql = 'INSERT INTO orders (order_id, parent_id, state, billing_first_name, billing_last_name, currency, date_created, date_modified, total, total_tax, payment_method, payment_method_title, transaction_id, customer_ip_address, created_via, customer_note, cart_hash, billing_company, billing_address_1 ,billing_address_2, billing_city, billing_state, billing_postcode, billing_country, billing_email, billing_phone, shipping_first_name, shipping_last_name, shipping_company, shipping_address_1, shipping_address_2, shipping_city, shipping_postcode, shipping_country )VALUES ({}, {}, {}, {}, {}, {}, NOW(), NOW(), {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
        order_details_id,
        order_details_parent_id,
        "'" + order_details_status + "'",
        "'" + billing_first_name + "'",
        "'" + billing_last_name + "'",
        "'" + order_details_currency + "'",
        # datetime.strptime(order_details_date_created, '%Y-%m-%dT%H:%M:%S'),
        # datetime.strptime(order_details_date_modified, '%Y-%m-%dT%H:%M:%S'),
        order_details_total,
        order_details_total_tax,
        "'" + order_details_payment_method + "'",
        "'" + order_details_payment_method_title + "'",
        "'" + order_details_transaction_id + "'",
        "'" + order_details_customer_ip_address + "'",
        "'" + order_details_created_via + "'",
        "'" + order_details_customer_note + "'",
        "'" + order_details_cart_hash + "'",
        "'" + billing_company + "'",
        "'" + billing_address_1 + "'",
        "'" + billing_address_2 + "'",
        "'" + billing_city + "'",
        "'" + billing_state + "'",
        "'" + billing_postcode + "'",
        "'" + billing_country + "'",
        "'" + billing_email + "'",
        "'" + billing_phone + "'",
        "'" + shipping_first_name + "'",
        "'" + shipping_last_name + "'",
        "'" + shipping_company + "'",
        "'" + shipping_address_1 + "'",
        "'" + shipping_address_2 + "'",
        "'" + shipping_city + "'",
        #"'" + shipping_state + "'",
        "'" + shipping_postcode + "'",
        "'" + shipping_country + "'"
    )
    db.engine.execute(sql)
    print(jsonify(order_details))
    return jsonify({
        'success': True,
        'msg': 'order record is create in blcokchain '
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
