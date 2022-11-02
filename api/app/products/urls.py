import json

from . import products_bp
from .views import ProductView
from app import websock

@products_bp.route('/add', methods=['POST'])
def create_product():
    """route to create a product"""
    return ProductView().create_product()


@products_bp.route('/get/<id>', methods=['GET'])
def get_product(id):
    """route to get a product"""
    return ProductView().get_product(id)


@products_bp.route('/get-all', methods=['GET'])
def ge_products():
    """route to get all products"""
    return ProductView().get_all()


@products_bp.route('/update/<id>', methods=['PUT'])
def update_product(id):
    """route to update a product"""
    return ProductView().update_product(id)


@products_bp.route('/delete/<id>', methods=['DELETE'])
def delete_product(id):
    """route to delete a product"""
    return ProductView().delete_product(id)


@products_bp.route('/sell/<id>', methods=['DELETE'])
def sell_product(id):
    """route to simulate sale of a product"""
    return ProductView().sell_product(id)

# @websock.route('/reorder')
# def request_reorder(sock):
#     while True:
#         print(f"socket id ====>{sock.environ['HTTP_SEC_WEBSOCKET_KEY']}")
#         socket_id = sock.environ['HTTP_SEC_WEBSOCKET_KEY']
#         sock.send("connected success!")
#         billing_data = sock.receive()
#         print(f"Billing data ---->", billing_data)
#         json_str = json.loads(billing_data)
#         json_str['socket_id'] = socket_id
#         billing_response = BillingAPI().receive_connection(json_str)

#         sock.send("received")
       