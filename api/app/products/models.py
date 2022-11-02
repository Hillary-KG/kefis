from datetime import datetime
from pytz import timezone
import MySQLdb

from app import db

class Product(db.Model):
    """product model definition"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    qtty = db.Column(db.Integer, default=0)
    reoder_level = db.Column(db.Integer, default=5)
    orders = db.relationship('Order', backref='product', lazy=True)
    reorders = db.relationship('ReOrder', backref='product', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone('Africa/Nairobi')))
    updated_at = db.Column(db.DateTime, default=datetime.now(tz=timezone('Africa/Nairobi')))


    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'qtty': self.qtty,
            'reorder_level': self.reoder_level,
            'orders': [
                order.serializer
                for order in self.orders
                ],
            'rorders': [
                reorder.serializer
                for reorder in self.reorders
                ],
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    
    def add(self, data):
        """add product record to the db"""
        try:
            product = Product(**data)

            db.session.add(product)
            try:
                db.session.commit()
            except MySQLdb.IntegrityError as e:
                # log exception
                print(str(e))
                return None 

            # refresh the inserted object and get id
            db.session.refresh(product)
            if not product.id:
                return None

            return product.id
        except MySQLdb.IntegrityError as e:
            # log exception
            print(str(e))
            return None 

    def get_one(self, id):
        """retrieve product from db by id"""
        product = Product.query.filter_by(id=id).first()
        if not product:
            return None
        
        return product.serializer
    
    def get_all(self):
        """retieve all products from the db"""
        products = Product.query.all()

        if not products:
            return None

        return [
            product.serializer
            for product in products
        ]

    def update_product(self, id, data):
        """update product record in db by id"""
        product = Product.query.filter_by(id=id).update(data)
        if not product:
            return None
        db.session.commit()

        return product

    def delete_product(self, id):
        """delete product from the db by id"""
        product = Product.query.filter_by(id=id).first()

        if not product:
            return None
        db.session.delete(product)
        db.session.commit()
        product = Product.query.filter_by(id=id).first()

        if product:
            return None

        return True