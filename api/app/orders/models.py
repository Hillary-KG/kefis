from datetime import datetime
from pytz import timezone
import MySQLdb

from app import db
from .generate_id import generateId

class Order(db.Model):
    """order data model definition"""
    id = db.Column(db.String(6), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    status = db.Column(db.Integer, default=0) #0-unfulfilled 1-fullfilled
    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone('Africa/Nairobi')))
    updated_at = db.Column(db.DateTime, default=datetime.now(tz=timezone('Africa/Nairobi')))


    @property
    def serializer(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    
    def add(self, data):
        """add order record to the db"""
        try:
            data['id'] = generateId()
            
            order = Order(**data)

            db.session.add(order)
            try:
                db.session.commit()
            except MySQLdb.IntegrityError as e:
                # log exception
                print(str(e))
                return None 

            # refresh the inserted object and get id
            db.session.refresh(order)
            if not order.id:
                return None

            return order.id
        except MySQLdb.IntegrityError as e:
            # log exception
            print(str(e))
            return None 

    def get_one(self, id):
        """retrieve order from db by id"""
        order = Order.query.filter_by(id=id).first()
        if not order:
            return None
        
        return order.serializer
    
    def get_all(self):
        """retieve all orders from the db"""
        orders = Order.query.all()

        if not orders:
            return None

        return [
            order.serializer
            for order in orders
        ]
    
    def get_unfulfilled(self, product_id):
        """retieve all orders from the db"""
        orders = Order.query.filter_by(status=0, product_id=product_id).all()

        if not orders:
            return None

        return [
            order.serializer
            for order in orders
        ]

    def update_order(self, id, data):
        """update order record in db by id"""
        order = Order.query.filter_by(id=id).update(data)
        if not order:
            return None
        db.session.commit()

        return order

    def delete_order(self, id):
        """delete order from the db by id"""
        order = Order.query.filter_by(id=id).first()

        if not order:
            return None
        db.session.delete(order)
        db.session.commit()
        order = Order.query.filter_by(id=id).first()

        if order:
            return None

        return True