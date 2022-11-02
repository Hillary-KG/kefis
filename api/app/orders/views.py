from flask import jsonify, request
from flask_jwt_extended import current_user

from .models import Order

class OrdersView:
    """holds the view function logic order: manipulation of orders"""

    def create_order(self):
        """view func() to create a new order"""
        try:
            request_data = request.get_json(force=True)
            if not request_data:
                return jsonify({
                    'success': False,
                    'msg': "Bad request! No order data submitted"
                }), 400

            order_id = Order().add(request_data)

            if not order_id:
                return jsonify({
                    'success': False,
                    'msg': "could not create order! Try again" 
                }), 400
            
            return jsonify({
                    'success': True,
                    'msg': "order created successfully!"
                }), 201
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    
    def get_order(self, id):
        """view func() to get one order"""
        try:
            order = Order().get_one(id)
            if not order:
                return jsonify({
                    'success': False,
                    'msg': "order not found"
                }), 404
            return jsonify({
                'success': True,
                'msg': "order found",
                'data': order
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    
    def get_all(self):
        """view func() to gett all orders"""
        try:
            orders = Order().get_all()
            if not orders:
                return jsonify({
                    'success': False,
                    'msg': "no orders found"
                }), 404
            return jsonify({
                'success': True,
                'msg': f"{len(orders)} order found",
                'data': orders
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    
    def delete_order(self, id):
        """view func() to delete order"""
        try:
            orders_dedleted = Order().delete_order(id)
            if not orders_dedleted:
                return jsonify({
                    'success': False,
                    'msg': "could not delete order. try again"
                })
            return jsonify({
                'success': True,
                'msg': "order deleted successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def update_order(self, id):
        """view func() to update order"""
        try:
            update_data = request.get_json(force=True)
            if not update_data:
                return jsonify({
                    'success': False,
                    'msg': "no update data submitted"
                }), 400

            updated_ = Order().update_order(id, update_data)
            if not updated_:
                return jsonify({
                    'success': False,
                    'msg': "failed. could not update order",
                }), 400
                
            return jsonify({
                'success': True,
                'msg': "order updated successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def sale(self):
        """view func() to create a new order"""
        try:
            pass
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500
    
    def update_order(self, id):
        """view func() to create a new order"""
        try:
            if not current_user:
                return jsonify({
                    'success': False,
                    'msg': "Unauthorized"
                }), 401
            
            update_data = request.get_json(force=True)
            if not update_data:
                return jsonify({
                    'success': False,
                    'msg': "no order data submitted"
                }), 400

            updated_ = Order().update_order(id, update_data)
            if not updated_:
                return jsonify({
                    'success': False,
                    'msg': "failed. could not update order",
                }), 400
                
            return jsonify({
                'success': True,
                'msg': "order updated successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500