from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Gender_simple_cambio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
       
    def __repr__(self):
        return '<Gender %r>' % self.type

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
        }
