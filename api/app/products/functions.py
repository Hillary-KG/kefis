from app.reorders.models import ReOrder
from app.orders.models import Order
from app.products.models import Product

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.orders.generate_id import generateId

from app import db
def make_reorder(product_id):
    try:
        pass
    except Exception as e:

        return False
        
def run_sale(product_id, qty):
    """sale db transaction"""
    try:
        session = Session(db.engine)
        with session.begin():
            order = Order(**{
                'id': generateId(),
                'product_id': product_id
            })
            session.add(order)
            product = session.execute(select(Product).filter_by(id=product_id)).scalar_one()
            product.qtty = qty - 1
            order = session.execute(select(Order).filter_by(id=order.id)).scalar_one()
            order.status = 1
    except Exception as e:
        print(str(e))
        session.rollback()
        return False
    else:
        session.close()
        reorder_req = reorder(product_id)
        if not reorder_req:
            return False
        return True


def reorder(product_id):
    """make reorder if reorder limit is reached"""
    product = Product.query.filter_by(id=product_id).first()

    if product.qtty <= product.reoder_level:
        reorder_ = ReOrder.query.filter_by(product_id=product_id, status=0).first()
        if not reorder_:
            reorder_ = ReOrder(product_id=product_id, name=product.name)
            db.session.add(reorder_)
            db.session.commit()

            db.session.refresh(reorder_)
            if not reorder_.id:
                return None
            return reorder_.id
        else:
            return True
    else:
        return True

