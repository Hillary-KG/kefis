from . import orders_bp
from .views import OrdersView

@orders_bp.route('/add', methods=['POST'])
def create_order():
    """route to create an order"""
    return OrdersView().create_order()


@orders_bp.route('/get/<id>', methods=['GET'])
def get_order(id):
    """route to get an order"""
    return OrdersView().get_order(id)


@orders_bp.route('/get-all', methods=['GET'])
def ge_orders():
    """route to get all orders"""
    return OrdersView().get_all()


@orders_bp.route('/update/<id>', methods=['PUT'])
def update_order(id):
    """route to update an order"""
    return OrdersView().update_order(id)


@orders_bp.route('/delete/<id>', methods=['DELETE'])
def delete_order(id):
    """route to delete an order"""
    return OrdersView().delete_order(id)


