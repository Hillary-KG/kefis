from flask import Blueprint


reorders_bp = Blueprint('reorders_bp', __name__, url_prefix='/reorders')


from . import urls