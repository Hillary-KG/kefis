from flask import jsonify, request
from flask_jwt_extended import current_user

from app.orders.models import Order

from .models import Product
from .functions import run_sale

class ProductView:
    """holds the view function logic product:::: manipulation of product objects"""

    def create_product(self):
        """view func() to create a new product"""
        try:
            request_data = request.get_json(force=True)
            if not request_data:
                return jsonify({
                    'success': False,
                    'msg': "Bad request! No product data submitted"
                }), 400

            product_id = Product().add(request_data)

            if not product_id:
                return jsonify({
                    'success': False,
                    'msg': "could not create product! Try again" 
                }), 400
            
            return jsonify({
                    'success': True,
                    'msg': "product created successfully!"
                }), 201
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500
 
    def get_product(self, id):
        """view func() to get one product"""
        try:
            product = Product().get_one(id)
            if not product:
                return jsonify({
                    'success': False,
                    'msg': "product not found"
                }), 404
            return jsonify({
                'success': True,
                'msg': "product found",
                'data': product
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500
    
    def get_all(self):
        """view func() to get all products"""
        try:
            products = Product().get_all()
            if not products:
                return jsonify({
                    'success': False,
                    'msg': "no products found"
                }), 404
            return jsonify({
                'success': True,
                'msg': f"{len(products)} product found",
                'data': products
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500
  
    def delete_product(self, id):
        """view func() to delete product"""
        try:
            products_dedleted = Product().delete_product(id)
            if not products_dedleted:
                return jsonify({
                    'success': False,
                    'msg': "could not delete product. try again"
                })
            return jsonify({
                'success': True,
                'msg': "product deleted successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def update_product(self, id):
        """view func() to update product"""
        try:
            update_data = request.get_json(force=True)
            if not update_data:
                return jsonify({
                    'success': False,
                    'msg': "no update data submitted"
                }), 400

            updated_ = Product().update_product(id, update_data)
            if not updated_:
                return jsonify({
                    'success': False,
                    'msg': "failed. could not update product",
                }), 400
                
            return jsonify({
                'success': True,
                'msg': "product updated successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def sell_product(self, id):
        """view func() to simulate sale of a product"""
        try:
            if not current_user:
                return jsonify({
                    'success': False,
                    'msg': "Unauthorized"
                }), 401
            
            # fetch product:
            product = Product().get_one(int(id))
            if not product:
                return jsonify({
                    'success': False,
                    'msg': "invalid product"
                }), 400
            reorder_level = product.get('qtty')
            qtty = product.get('qtty')

            unfulfillled = Order().get_unfulfilled(id)
            if unfulfillled:
                return jsonify({
                    'success': False,
                    'msg': "unfulfilled orders cannot be more than one!"
                }), 400
            # create order
            # order_id = Order().add({
            #     'product_id': id
            # })
            # if not order_id:
            #     return jsonify({
            #         'success': False,
            #         'msg': "could not generate order"
            #     }), 404

            if qtty == 0:
                return jsonify({
                    'success': False,
                    'msg': "product not available for sale"
                }), 404

            # updated_ = Product().update_product(id, {'qtty': qtty - 1})
            # if not updated_:
            #     return jsonify({
            #         'success': False,
            #         'msg': "sale failed. try again",
            #     }), 400
            # # update order 
            # order = Order().update_order(
            #     order_id,
            #     {
            #         'status': 1
            #     }
            # )
            # if not order:
            #     return jsonify({
            #         'success': False,
            #         'msg': "sale failed. could not update order",
            #     }), 400
            # make a reorder if reorder level reached
            # if qtty == reorder_level:
            #     pass
            if not run_sale(id, qtty):
                return jsonify({
                    'success': False,
                    'msg': "sale failed",
                }), 400

            return jsonify({
                'success': True,
                'msg': "product sale successful"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500