import json

import requests
from flask import jsonify, app, request
from sqlalchemy import desc, func, and_

from model import Orders, Inventory, db

user_name = "pyrarc.app"
user_passwd = "dOidZQSGR09BnHROt4ss#NT3"
end_point_url_posts = "https://store.pyrarc.com/wp-json/jwt-auth/v1/token"

payload = {
    "username": user_name,
    "password": user_passwd
}


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code


# 獲取最新庫存
def getEndInvertory(user_id=None, product_id=None):
    invertory_info = Inventory.query.filter_by(user_id=user_id, product_id=product_id).order_by(
        desc(Inventory.id)).limit(
        1).all()
    return invertory_info[0].ending_inventory


# 獲取最新庫存
def getInvertoryNow(user_id=None, product_id=None, adj_amount=None):
    invertory_info = Inventory.query.filter_by(user_id=user_id, product_id=product_id).order_by(
        desc(Inventory.id)).limit(
        1).all()
    if invertory_info:
        beging_inventory = invertory_info[0].ending_inventory
        ending_inventory = beging_inventory + adj_amount
    else:
        beging_inventory = 0
        ending_inventory = adj_amount
    return beging_inventory, ending_inventory


# 查詢最新庫存by客戶ＩＤ跟產品號碼
def inventory(customer_id: int):
    # inventories = Inventory.query.filter_by(user_id=customer_id, product_id=product_id).order_by(desc(Inventory.id)).limit(1).all()
    #inventories = db.session.query(func.max(Inventory.id), Inventory.user_id, Inventory.product_id,Inventory.ending_inventory).filter_by(user_id=customer_id).group_by(Inventory.id,Inventory.user_id,Inventory.product_id,Inventory.ending_inventory).all()
    subq = db.session.query(Inventory.user_id, Inventory.product_id, func.max(Inventory.id).label('max_id')).group_by(Inventory.user_id, Inventory.product_id).subquery('t2')

    inventories = db.session.query(Inventory).filter_by(user_id=customer_id).join(subq, and_(Inventory.user_id == subq.c.user_id, Inventory.id == subq.c.max_id)).all()

    r = requests.post(end_point_url_posts, data=payload)
    jwt_info = r.content.decode("utf-8").replace("'", '"')
    data = json.loads(jwt_info)
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)
    token = data['token']
    Auth_token = "Bearer " + token

    my_headers = {'Authorization': Auth_token}

    if inventories:
        # productlist = wcapi.get("products", params={"per_page": 20}).json()
        for inv in inventories:
            response_productlist = requests.get('https://store.pyrarc.com/wp-json/wc/v3/products/' + str(inv.product_id), data=payload, headers=my_headers)
            productlist = json.loads(response_productlist.content.decode("utf-8").replace("'", '"'))
            inv.product_name = productlist["name"]
        # inventory = inventories[0]
        return jsonify([inventory.to_json_ext() for inventory in inventories])
    else:
        return jsonify({
            'message': 'data is not exist'
        })


# 新增庫存
def inventoryadd():
    req = request.data.decode("utf-8").replace("'", '"')
    data = json.loads(req)
    user_id = data['user_id']
    adj_amount = data['adj_amount']
    order_id = data['order_id']
    product_id = data['product_id']
    create_by = data['create_by']
    order_source = data['order_source']
    # 獲取最新的庫存
    beging_inventory, ending_inventory = getInvertoryNow(user_id, product_id, adj_amount)
    inventory = Inventory(user_id, beging_inventory, ending_inventory, adj_amount, order_id, product_id, create_by,
                          order_source, '', '', '', '', '', '', '', '', '')
    db.session.add(inventory)
    db.session.commit()
    return jsonify({
        'success': True,
        'msg': 'inventory is added now ',
        'data': data
    })


# 指配派送
def inventorydelivery():
    req = request.data.decode("utf-8").replace("'", '"')
    data = json.loads(req)
    user_id = data['user_id']
    adj_amount = data['adj_amount']
    product_id = data['product_id']
    create_by = data['create_by']
    order_source = data['order_source']
    shipping_first_name = data['shipping_first_name']
    shipping_last_name = data['shipping_last_name']
    shipping_company = data['shipping_company']
    shipping_address_1 = data['shipping_address_1']
    shipping_city = data['shipping_city']
    shipping_postcode = data['shipping_postcode']
    shipping_country = data['shipping_country']
    shipping_phone = data['shipping_phone']
    remark = data['remark']
    # 判斷配送的數量是否超過現有庫存
    Inventory_now = getEndInvertory(user_id, product_id)
    if Inventory_now < adj_amount * -1:
        return jsonify({
            'message': 'Quantities is not enough'
        })
    # 獲取最新的庫存
    beging_inventory, ending_inventory = getInvertoryNow(user_id, product_id, adj_amount)
    inventory = Inventory(user_id, beging_inventory, ending_inventory, adj_amount, 0, product_id, create_by,
                          order_source, shipping_first_name, shipping_last_name, shipping_company, shipping_address_1,
                          shipping_city, shipping_postcode, shipping_country, shipping_phone, remark)
    db.session.add(inventory)
    db.session.commit()
    return jsonify({
        'success': True,
        'msg': 'inventory is added now ',
        'data': data
    })


def inventorydelivery():
    req = request.data.decode("utf-8").replace("'", '"')
    data = json.loads(req)
    user_id = data['user_id']
    adj_amount = data['adj_amount']
    product_id = data['product_id']
    create_by = data['create_by']
    order_source = data['order_source']
    shipping_first_name = data['shipping_first_name']
    shipping_last_name = data['shipping_last_name']
    shipping_company = data['shipping_company']
    shipping_address_1 = data['shipping_address_1']
    shipping_city = data['shipping_city']
    shipping_postcode = data['shipping_postcode']
    shipping_country = data['shipping_country']
    shipping_phone = data['shipping_phone']
    remark = data['remark']
    # 判斷配送的數量是否超過現有庫存
    Inventory_now = getEndInvertory(user_id, product_id)
    if Inventory_now < adj_amount * -1:
        return jsonify({
            'message': 'Quantities is not enough'
        })
    # 獲取最新的庫存
    beging_inventory, ending_inventory = getInvertoryNow(user_id, product_id, adj_amount)
    inventory = Inventory(user_id, beging_inventory, ending_inventory, adj_amount, 0, product_id, create_by,
                          order_source, shipping_first_name, shipping_last_name, shipping_company, shipping_address_1,
                          shipping_city, shipping_postcode, shipping_country, shipping_phone, remark)
    db.session.add(inventory)
    db.session.commit()
    token = 'M5g5yVHMV2gc6iRvs1xu5Bsb9OEj0Wux8pQcKknldMo'
    msg = '用戶已指派寄送，請登入平台，輸入物流單號 https://storeapi.pyrarc.com/backend/inventorylist?mid=' + str(inventory.id)
    lineNotifyMessage(token, msg)
    return jsonify({
        'success': True,
        'msg': 'inventory is added now ',
        'data': data
    })


# 獲取五筆指派紀錄
def inventoryhistory(customer_id: int):
    inventories = Inventory.query.filter_by(user_id=customer_id, order_id=0).order_by(
        desc(Inventory.id)).limit(5).all()
    if inventories:
        for inv in inventories:
            inv.adj_amount = int(inv.adj_amount) * -1
        return jsonify([inventory.to_json() for inventory in inventories])
    else:
        return jsonify({
            'message': 'data is not exist'
        })
