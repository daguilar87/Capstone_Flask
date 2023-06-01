from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from secrets import token_hex

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, default=None)
  

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password) 
        self.token = token_hex(16)

    def saveUser(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'token' : self.token
        }


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details1 = db.Column(db.String, nullable=True)
    details2 = db.Column(db.String, nullable=True)
    details3 = db.Column(db.String, nullable=True)
    details4 = db.Column(db.String, nullable=True)
    details5 = db.Column(db.String, nullable=True)
    details6 = db.Column(db.String, nullable=True)
    details7 = db.Column(db.String, nullable=True)
    details8 = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, details1, details2, details3, details4, details5, details6, details7, details8, img_url,name, price=0):
        self.details1 = details1
        self.details2 = details2
        self.details3 = details3
        self.details4 = details4
        self.details5 = details5
        self.details6 = details6
        self.details7 = details7
        self.details8 = details8
        img_url = img_url
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'details1': self.details1,
            'details2': self.details2,
            'details3': self.details3,
            'details4': self.details4,
            'details5': self.details5,
            'details6': self.details6,
            'details7': self.details7,
            'details8': self.details8,
            'img_url' : self.img_url,
            'name': self.name,
            'price': self.price,
            'date_created': self.date_created,
        }

    
    def saveService(self):
        db.session.add(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    def deleteService(self):
        db.session.delete(self)
        db.session.commit()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    services = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=True)
          
    def __init__(self, name, phone, email, services, message):
        self.name = name
        self.phone = phone
        self.email = email
        self.services = services
        self.message = message

    def saveCon(self):
        db.session.add(self)
        db.session.commit()

    def deletecontact(self):
        db.session.delete(self)
        db.session.commit()


class Addons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    det1 = db.Column(db.String)
    det2 = db.Column(db.String)
    det3 = db.Column(db.String)
    det4 = db.Column(db.String)

    def __init__(self, det1, det2, det3, det4):
        self.det1 = det1
        self.det2 = det2
        self.det3 = det3
        self.det4 = det4

    def to_dict(self):
        return {
            'id' : self.id,
            'det1' : self.det1,
            'det2' : self.det2,
            'det3' : self.det3,
            'det4' : self.det4
        }
    
    def savedet(self):
        db.session.add(self)
        db.session.commit()

    def saveadd(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
