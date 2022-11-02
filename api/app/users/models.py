from datetime import datetime
import  MySQLdb
from app import db
from pytz import timezone
from sqlalchemy import desc

class User(db.Model):
    """class defines the user model."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    user_type = db.Column(db.Integer, default=4) #2-store attendant, 1-warehse
    last_login = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone('Africa/Nairobi')))
    updated_at = db.Column(db.DateTime, default=datetime.now(tz=timezone('Africa/Nairobi')))


    @property
    def serializer(self):
        return {
            'id': self.id,
            'email': self.email,
            'user_type': self.user_type,
            'last_login': self.last_login,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def create(self, data):
        """add user record to the db"""
        try:
            user = User(**data)

            db.session.add(user)
            db.session.commit()
            # refresh the inserted object and get id
            db.session.refresh(user)
            if not user.id:
                return None

            return user.id
        except MySQLdb.IntegrityError as e:
            # log exception
            return None 

    def update_user(self, id, data):
        """
            edit user details method
            return user_id or None 
        """
        user = User.query.filter_by(id=id).update(data)

        if not user:
            return None
        db.session.commit()

        return user