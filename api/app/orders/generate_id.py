from sqlalchemy import desc

def generateId():
    from .models import Order
    orders = Order.query.order_by(desc(Order.created_at)).all()
    ids = sorted([order.id for order in orders], reverse=True)
    last = int(ids[0])
    new_id = str(last+1).zfill(6)

    return new_id