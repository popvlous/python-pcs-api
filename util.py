import json

import requests

token = "SEY3QW9ES2ZBbw=="

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}


class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def insertBlockChainOrder(order_details):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/orders/create"

    billing = order_details['billing']
    shipping = order_details['shipping']

    payload = {
        "order_id": order_details['id'],
        "parent_id": order_details['parent_id'],
        "state": order_details['status'],
        "billing_first_name": billing['first_name'],
        "billing_last_name": billing['last_name'],
        "currency": order_details['currency'],
        "version": order_details['version'],
        "date_created": order_details['date_created'],
        "date_modified": order_details['date_modified'],
        "total": order_details['total'],
        "total_tax": order_details['total_tax'],
        "customer_id": order_details['customer_id'],
        "order_key": "",
        "billing_company": billing['company'],
        "billing_address_1": billing['address_1'],
        "billing_address_2": billing['address_2'],
        "billing_city": billing['city'],
        "billing_state": billing['state'],
        "billing_postcode": billing['postcode'],
        "billing_country": billing['country'],
        "billing_email": billing['email'],
        "billing_phone": billing['phone'],
        "shipping_first_name": shipping['first_name'],
        "shipping_last_name": shipping['last_name'],
        "shipping_company": shipping['company'],
        "shipping_address_1": shipping['address_1'],
        "shipping_address_2": shipping['address_2'],
        "shipping_city": shipping['city'],
        "shipping_state": shipping['state'],
        "shipping_postcode": shipping['postcode'],
        "shipping_country": shipping['country'],
        "payment_method": order_details['payment_method'],
        "payment_method_title": order_details['payment_method_title'],
        "transaction_id": order_details['transaction_id'],
        "customer_ip_address": order_details['customer_ip_address'],
        "created_via": order_details['created_via'],
        "customer_note": order_details['customer_note'],
        "date_completed": "",
        "date_paid": "",
        "cart_hash": order_details['cart_hash'],
        "line_items_id": "",
        "line_items_name": "",
        "line_items_product_id": "",
        "line_items_variation_id": "",
        "line_items_quantity": "",
        "line_items_tax_class": "",
        "line_items_subtotal": "",
        "line_items_subtotal_tax": "",
        "line_items_total": "",
        "line_items_total_tax": "",
        "line_items_taxes": "",
        "line_items_sku": "",
        "line_items_price": "",
        "line_items_parent_name": ""
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content

def updateBlockChainOrder(order_details):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/orders/create"

    billing = order_details['billing']
    shipping = order_details['shipping']

    payload = {
        "order_id": order_details['id'],
        "parent_id": order_details['parent_id'],
        "state": order_details['status'],
        "billing_first_name": billing['first_name'],
        "billing_last_name": billing['last_name'],
        "currency": order_details['currency'],
        "version": order_details['version'],
        "date_created": order_details['date_created'],
        "date_modified": order_details['date_modified'],
        "total": order_details['total'],
        "total_tax": order_details['total_tax'],
        "customer_id": order_details['customer_id'],
        "order_key": "",
        "billing_company": billing['company'],
        "billing_address_1": billing['address_1'],
        "billing_address_2": billing['address_2'],
        "billing_city": billing['city'],
        "billing_state": billing['state'],
        "billing_postcode": billing['postcode'],
        "billing_country": billing['country'],
        "billing_email": billing['email'],
        "billing_phone": billing['phone'],
        "shipping_first_name": shipping['first_name'],
        "shipping_last_name": shipping['last_name'],
        "shipping_company": shipping['company'],
        "shipping_address_1": shipping['address_1'],
        "shipping_address_2": shipping['address_2'],
        "shipping_city": shipping['city'],
        "shipping_state": shipping['state'],
        "shipping_postcode": shipping['postcode'],
        "shipping_country": shipping['country'],
        "payment_method": order_details['payment_method'],
        "payment_method_title": order_details['payment_method_title'],
        "transaction_id": order_details['transaction_id'],
        "customer_ip_address": order_details['customer_ip_address'],
        "created_via": order_details['created_via'],
        "customer_note": order_details['customer_note'],
        "date_completed": "",
        "date_paid": "",
        "cart_hash": order_details['cart_hash'],
        "line_items_id": "",
        "line_items_name": "",
        "line_items_product_id": "",
        "line_items_variation_id": "",
        "line_items_quantity": "",
        "line_items_tax_class": "",
        "line_items_subtotal": "",
        "line_items_subtotal_tax": "",
        "line_items_total": "",
        "line_items_total_tax": "",
        "line_items_taxes": "",
        "line_items_sku": "",
        "line_items_price": "",
        "line_items_parent_name": ""
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content


def insertBlockChainLineItem(line_items):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/orderitem/create"

    payload = {
        "id": line_items.id,
        "order_id": line_items.order_id,
        "line_items_id": line_items.line_items_id,
        "line_items_name": line_items.line_items_name,
        "line_items_product_id": line_items.line_items_product_id,
        "line_items_variation_id": line_items.line_items_variation_id,
        "line_items_quantity": line_items.line_items_quantity,
        "line_items_tax_class": line_items.line_items_tax_class,
        "line_items_subtotal": line_items.line_items_subtotal,
        "line_items_subtotal_tax": line_items.line_items_subtotal_tax,
        "line_items_total": line_items.line_items_total,
        "line_items_total_tax": line_items.line_items_total_tax,
        "line_items_taxes": line_items.line_items_taxes if line_items.line_items_taxes else "",
        "line_items_sku": line_items.line_items_sku,
        "line_items_price": line_items.line_items_price,
        "line_items_parent_name": line_items.line_items_parent_name if line_items.line_items_parent_name else ""
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content


def insertBlockChainInventory(inventory):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/inventory/create"

    payload = {
        "id": inventory.id,
        "user_id": inventory.user_id,
        "beging_inventory": inventory.beging_inventory,
        "ending_inventory": inventory.ending_inventory,
        "adj_amount": inventory.adj_amount,
        "create_time": str(inventory.create_time),
        "modify_time": str(inventory.modify_time),
        "transaction_id": inventory.transaction_id if inventory.transaction_id else "",
        "order_id": inventory.order_id,
        "product_id": inventory.product_id,
        "create_by": inventory.create_by,
        "order_source": inventory.order_source,
        "location": inventory.location if inventory.location else "",
        "shipping_first_name": inventory.shipping_first_name,
        "shipping_last_name": inventory.shipping_last_name,
        "shipping_company": inventory.shipping_company,
        "shipping_address_1": inventory.shipping_address_1,
        "shipping_address_2": "",
        "shipping_city": inventory.shipping_city,
        "shipping_postcode": inventory.shipping_postcode,
        "shipping_country": inventory.shipping_country,
        "shipping_phone": inventory.shipping_phone,
        "shipment_number": inventory.shipment_number if inventory.shipment_number else "",
        "remark": inventory.remark
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code
