import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer)
    signup_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'age': self.age,
            'signup_date': self.signup_date.isoformat()
        }

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'


class Order(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'))
    quantity = db.Column(db.Integer)
    color = db.Column(db.String(64))

    # garment types
    is_tee = db.Column(db.Boolean)
    is_tank = db.Column(db.Boolean)
    is_hoodie = db.Column(db.Boolean)
    is_polo = db.Column(db.Boolean)
    is_hat = db.Column(db.Boolean)
    is_bag = db.Column(db.Boolean)
    is_other = db.Column(db.Boolean)

    # print locations
    is_front = db.Column(db.Boolean)
    is_back = db.Column(db.Boolean)
    is_sleeve = db.Column(db.Boolean)
    is_tag = db.Column(db.Boolean)

    # 0 = economy, 1 = standard, 2 = premium
    garment_quality = db.Column(db.Integer)

    has_artwork = db.Column(db.Boolean)
    is_hard_deadline = db.Column(db.Boolean)
    completion_date = db.Column(db.DateTime)
    order_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'quantity': self.quantity,
            'color': self.color,
            'is_tee': self.is_tee,
            'is_tank': self.is_tank,
            'is_hoodie': self.is_hoodie,
            'is_polo': self.is_polo,
            'is_hat': self.is_hat,
            'is_bag': self.is_bag,
            'is_other': self.is_other,
            'is_front': self.is_front,
            'is_back': self.is_back,
            'is_sleeve': self.is_sleeve,
            'is_tag': self.is_tag,
            'garment_quality': self.garment_quality,
            'has_artwork': self.has_artwork,
            'is_hard_deadline': self.is_hard_deadline,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None,
            'order_date': self.order_date.isoformat()
        }

    def __repr__(self):
        return f'<Order {self.id}>'