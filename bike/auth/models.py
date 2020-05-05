from bike import db,bcrypt
from datetime import datetime
from flask_login import UserMixin
from flask import flash

class Users(UserMixin,db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(15),nullable=False)
    user_email=db.Column(db.String(30),unique=True,index=True)
    user_pw=db.Column(db.String(60))
    register_date=db.Column(db.DateTime,default=datetime.now)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.user_pw,password)

    @classmethod
    def create_user(cls,user,email,password):
        usr=cls(user_name=user,
        user_email=email,
        user_pw=bcrypt.generate_password_hash(password).decode('utf-8')
        )

        db.session.add(usr)
        db.session.commit()
        return usr