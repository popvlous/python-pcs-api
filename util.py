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
    end_point_url_posts = "https://ccapi.stag.nexuera.com/orders/update"

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


def updateBlockChainLineItem(line_items):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/orderitem/update"

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
        "id": inventory.id if inventory.id else "",
        "user_id": inventory.user_id if inventory.user_id else "",
        "beging_inventory": inventory.beging_inventory if inventory.beging_inventory else "",
        "ending_inventory": inventory.ending_inventory if inventory.ending_inventory else "",
        "adj_amount": inventory.adj_amount if inventory.adj_amount else "",
        "create_time": str(inventory.create_time),
        "modify_time": str(inventory.modify_time),
        "transaction_id": inventory.transaction_id if inventory.transaction_id else "",
        "order_id": inventory.order_id if inventory.order_id else "",
        "product_id": inventory.product_id if inventory.product_id else "",
        "create_by": inventory.create_by if inventory.create_by else "",
        "order_source": inventory.order_source if inventory.order_source else "",
        "location": inventory.location if inventory.location else "",
        "shipping_first_name": inventory.shipping_first_name if inventory.shipping_first_name else "",
        "shipping_last_name": inventory.shipping_last_name if inventory.shipping_last_name else "",
        "shipping_company": inventory.shipping_company if inventory.shipping_company else "",
        "shipping_address_1": inventory.shipping_address_1 if inventory.shipping_address_1 else "",
        "shipping_address_2": "",
        "shipping_city": inventory.shipping_city if inventory.shipping_city else "",
        "shipping_postcode": inventory.shipping_postcode if inventory.shipping_postcode else "",
        "shipping_country": inventory.shipping_country if inventory.shipping_country else "",
        "shipping_phone": inventory.shipping_phone if inventory.shipping_phone else "",
        "shipment_number": inventory.shipment_number if inventory.shipment_number else "",
        "remark": inventory.remark if inventory.remark else ""
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content


def updateBlockChainInventory(inventory):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/inventory/update"

    payload = {
        "id": inventory.id if inventory.id else "",
        "user_id": inventory.user_id if inventory.user_id else "",
        "beging_inventory": inventory.beging_inventory if inventory.beging_inventory else "",
        "ending_inventory": inventory.ending_inventory if inventory.ending_inventory else "",
        "adj_amount": inventory.adj_amount if inventory.adj_amount else "",
        "create_time": str(inventory.create_time),
        "modify_time": str(inventory.modify_time),
        "transaction_id": inventory.transaction_id if inventory.transaction_id else "",
        "order_id": inventory.order_id if inventory.order_id else "",
        "product_id": inventory.product_id if inventory.product_id else "",
        "create_by": inventory.create_by if inventory.create_by else "",
        "order_source": inventory.order_source if inventory.order_source else "",
        "location": inventory.location if inventory.location else "",
        "shipping_first_name": inventory.shipping_first_name if inventory.shipping_first_name else "",
        "shipping_last_name": inventory.shipping_last_name if inventory.shipping_last_name else "",
        "shipping_company": inventory.shipping_company if inventory.shipping_company else "",
        "shipping_address_1": inventory.shipping_address_1 if inventory.shipping_address_1 else "",
        "shipping_address_2": "",
        "shipping_city": inventory.shipping_city if inventory.shipping_city else "",
        "shipping_postcode": inventory.shipping_postcode if inventory.shipping_postcode else "",
        "shipping_country": inventory.shipping_country if inventory.shipping_country else "",
        "shipping_phone": inventory.shipping_phone if inventory.shipping_phone else "",
        "shipment_number": inventory.shipment_number if inventory.shipment_number else "",
        "remark": inventory.remark if inventory.remark else ""
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content


def insertBlockChainDelivery(delivery):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/delivery/create"

    payload = {
        "id": delivery.id if delivery.id else "",
        "user_id": delivery.user_id if delivery.user_id else "",
        "create_time": str(delivery.create_time),
        "modify_time": str(delivery.modify_time),
        "create_by": delivery.create_by if delivery.create_by else "",
        "order_source": delivery.order_source if delivery.order_source else "",
        "location": delivery.location if delivery.location else "",
        "shipping_first_name": delivery.shipping_first_name if delivery.shipping_first_name else "",
        "shipping_last_name": delivery.shipping_last_name if delivery.shipping_last_name else "",
        "shipping_company": delivery.shipping_company if delivery.shipping_company else "",
        "shipping_address_1": delivery.shipping_address_1 if delivery.shipping_address_1 else "",
        "shipping_address_2": delivery.shipping_address_2 if delivery.shipping_address_2 else "",
        "shipping_city": delivery.shipping_city if delivery.shipping_city else "",
        "shipping_state": delivery.shipping_state if delivery.shipping_state else "",
        "shipping_postcode": delivery.shipping_postcode if delivery.shipping_postcode else "",
        "shipping_country": delivery.shipping_country if delivery.shipping_country else "",
        "shipping_phone": delivery.shipping_phone if delivery.shipping_phone else "",
        "shipment_number": delivery.shipment_number if delivery.shipment_number else "",
        "remark": delivery.remark if delivery.remark else ""
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content


def updateBlockChainDelivery(delivery):
    end_point_url_posts = "https://ccapi.stag.nexuera.com/delivery/update"

    payload = {
        "id": delivery.id,
        "user_id": delivery.user_id,
        "create_time": delivery.create_time,
        "modify_time": delivery.modify_time,
        "create_by": delivery.create_by,
        "order_source": delivery.order_source,
        "location": delivery.location,
        "shipping_first_name": delivery.shipping_first_name,
        "shipping_last_name": delivery.shipping_last_name,
        "shipping_company": delivery.shipping_company,
        "shipping_address_1": delivery.shipping_address_1,
        "shipping_address_2": delivery.shipping_address_2,
        "shipping_city": delivery.shipping_city,
        "shipping_state": delivery.shipping_state,
        "shipping_postcode": delivery.shipping_postcode,
        "shipping_country": delivery.shipping_country,
        "shipping_phone": delivery.shipping_phone,
        "shipment_number": delivery.shipment_number,
        "remark": delivery.remark
    }

    r = requests.post(end_point_url_posts, headers=headers, data=json.dumps(payload), verify=False)
    return r.status_code, r.content
