from app.reorders.models import ReOrder
from app.orders.models import Order
from app.products.models import Product

from app import db
def make_reorder(product_id):
    try:
        pass
    except Exception as e:

        return False
        

def run_sale(product_id, qty):
    """sale db transaction"""
    try:
        with db.session.begin():
            order = Order({
                'product_id': product_id
            })
            print("order>>", order)

            db.session.add(order)
            Product.query.filter_by(id=product_id).update({
                'qtty': qty
            })
            order.update({
                'status': 1
            })
    except Exception as e:
        print(str(e))
        db.session.close()
        return False
    else:
        db.session.close()
        return True


        
