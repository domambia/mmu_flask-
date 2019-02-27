from app import db  

#User models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique = True, index = True)
    username = db.Column(db.String(32), unique = True)
    email = db.Column(db.String(100), unique=True)
    encrypted_password =  db.Column(db.String(128))

 