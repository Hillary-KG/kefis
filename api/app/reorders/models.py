from datetime import datetime
from pytz import timezone
import MySQLdb

from app import db

class ReOrder(db.Model):
    """Re-Order data model definition"""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Integer, default=0) #0-unprocessed 1-processed
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
        """add reorder record to the db"""
        try:
            reorder = ReOrder(**data)

            db.session.add(reorder)
            try:
                db.session.commit()
            except MySQLdb.IntegrityError as e:
                # log exception
                print(str(e))
                return None 

            # refresh the inserted object and get id
            db.session.refresh(reorder)
            if not reorder.id:
                return None

            return reorder.id
        except MySQLdb.IntegrityError as e:
            # log exception
            return None 

    def get_one(self, id):
        """retrieve reorder from db by id"""
        reorder = ReOrder.query.filter_by(id=id).first()
        if not reorder:
            return None
        
        return reorder.serializer
    
    def get_all(self):
        """retieve all reorders from the db"""
        reorders = ReOrder.query.all()

        if not reorders:
            return None

        return [
            reorder.serializer
            for reorder in reorders
        ]
    
    def get_unfulfilled(self):
        """retieve all reorders from the db"""
        reorders = ReOrder.query.filter_by(status=0).all()

        if not reorders:
            return None

        return [
            reorder.serializer
            for reorder in reorders
        ]

    def update_reorder(self, id, data):
        """update reorder record in db by id"""
        reorder = ReOrder.query.filter_by(id=id).update(data)
        if not reorder:
            return None
        db.session.commit()

        return reorder

    def delete_reorder(self, id):
        """delete reorder from the db by id"""
        reorder = ReOrder.query.filter_by(id=id).first()

        if not reorder:
            return None
        db.session.delete(reorder)
        db.session.commit()
        reorder = ReOrder.query.filter_by(id=id).first()

        if reorder:
            return None

        return True