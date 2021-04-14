import json

from flask import jsonify, app, request
from sqlalchemy import desc

from model import Orders, Inventory, db


# 獲取最新庫存
def getEndInvertory(user_id=None, product_id=None):
    invertory_info = Inventory.query.filter_by(user_id=user_id, product_id=product_id).order_by(
        desc(Inventory.id)).limit(
        1).all()
    return invertory_info[0].ending_Inventory


# 獲取最新庫存
def getInvertoryNow(user_id=None, product_id=None, adj_amount=None):
    invertory_info = Inventory.query.filter_by(user_id=user_id, product_id=product_id).order_by(
        desc(Inventory.id)).limit(
        1).all()
    beging_inventory = invertory_info[0].ending_Inventory
    ending_Inventory = beging_inventory + adj_amount
    return beging_inventory, ending_Inventory


# 查詢最新庫存by客戶ＩＤ跟產品號碼
def inventory(customer_id: int, product_id: int):
    inventories = Inventory.query.filter_by(user_id=customer_id, product_id=product_id).order_by(
        desc(Inventory.id)).limit(1).all()
    if inventories:
        inventory = inventories[0]
        return jsonify(inventory.to_json())
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
    beging_inventory, ending_Inventory = getInvertoryNow(user_id, product_id, adj_amount)
    inventory = Inventory(user_id, beging_inventory, ending_Inventory, adj_amount, order_id, product_id, create_by,
                          order_source, '', '', '', '', '', '', '', '', '')
    db.session.add(inventory)
    db.session.commit()
    return jsonify({
        'success': True,
        'msg': 'inventory is added now ',
        'data': data
    })


# 只配派送
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
    beging_inventory, ending_Inventory = getInvertoryNow(user_id, product_id, adj_amount)
    inventory = Inventory(user_id, beging_inventory, ending_Inventory, adj_amount, 0, product_id, create_by,
                          order_source, shipping_first_name, shipping_last_name, shipping_company, shipping_address_1,
                          shipping_city, shipping_postcode, shipping_country, shipping_phone, remark)
    db.session.add(inventory)
    db.session.commit()
    return jsonify({
        'success': True,
        'msg': 'inventory is added now ',
        'data': data
    })
