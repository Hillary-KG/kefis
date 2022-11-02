from . import reorders_bp
from .views import ReordersView

@reorders_bp.route('/add', methods=['POST'])
def create_reorder():
    """route to create a reorder"""
    return ReordersView().create_reorder()


@reorders_bp.route('/get/<id>', methods=['GET'])
def get_reorder(id):
    """route to get a reorder"""
    return ReordersView().get_reorder(id)


@reorders_bp.route('/get-all', methods=['GET'])
def ge_reorders():
    """route to get all reorders"""
    return ReordersView().get_all()


@reorders_bp.route('/update/<id>', methods=['PUT'])
def update_reorder(id):
    """route to update a reorder"""
    return ReordersView().update_reorder(id)


@reorders_bp.route('/delete/<id>', methods=['DELETE'])
def delete_reorder(id):
    """route to delete a reorder"""
    return ReordersView().delete_reorder(id)


