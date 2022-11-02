from flask import jsonify, request
from flask_jwt_extended import current_user

from .models import ReOrder

class ReordersView:
    """holds the view function logic reorder: manipulation of reorders"""

    def create_reorder(self):
        """view func() to create a new re-order"""
        try:
            request_data = request.get_json(force=True)
            if not request_data:
                return jsonify({
                    'success': False,
                    'msg': "Bad request! No reorder data submitted"
                }), 400

            reorder_id = ReOrder().add(request_data)

            if not reorder_id:
                return jsonify({
                    'success': False,
                    'msg': "could not create re-order! Try again" 
                }), 400
            
            return jsonify({
                    'success': True,
                    'msg': "re-order created successfully!"
                }), 201
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    
    def get_reorder(self, id):
        """view func() to get one re-order"""
        try:
            reorder = ReOrder().get_one(id)
            if not reorder:
                return jsonify({
                    'success': False,
                    'msg': "re-order not found"
                }), 404
            return jsonify({
                'success': True,
                'msg': "re-order found",
                'data': reorder
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    
    def get_all(self):
        """view func() to gett all reorders"""
        try:
            reorders = ReOrder().get_all()
            if not reorders:
                return jsonify({
                    'success': False,
                    'msg': "no reorders found"
                }), 404
            return jsonify({
                'success': True,
                'msg': f"{len(reorders)} reorder found",
                'data': reorders
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    
    def delete_reorder(self, id):
        """view func() to delete re-order"""
        try:
            reorders_dedleted = ReOrder().delete_reorder(id)
            if not reorders_dedleted:
                return jsonify({
                    'success': False,
                    'msg': "could not delete reorder. try again"
                })
            return jsonify({
                'success': True,
                'msg': "re-order deleted successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def update_reorder(self, id):
        """view func() to update re-order"""
        try:
            update_data = request.get_json(force=True)
            if not update_data:
                return jsonify({
                    'success': False,
                    'msg': "no update data submitted"
                }), 400

            updated_ = ReOrder().update_reorder(id, update_data)
            if not updated_:
                return jsonify({
                    'success': False,
                    'msg': "failed. could not update re-order",
                }), 400
                
            return jsonify({
                'success': True,
                'msg': "re-order updated successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def sale(self):
        """view func() to create a new re-order"""
        try:
            pass
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500
    
    def update_reorder(self, id):
        """view func() to create a new re-order"""
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
                    'msg': "no reorder data submitted"
                }), 400

            updated_ = ReOrder().update_reorder(id, update_data)
            if not updated_:
                return jsonify({
                    'success': False,
                    'msg': "failed. could not update re-order",
                }), 400
                
            return jsonify({
                'success': True,
                'msg': "re-order updated successfully"
            }), 200
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500