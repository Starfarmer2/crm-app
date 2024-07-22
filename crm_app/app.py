from flask import Flask, jsonify, request
from models import db, User, Order
import datetime
import uuid

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "postgresql://postgres:postgres@db:5432/crm"

engine = create_engine(DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database {engine.url.database} created successfully.")
else:
    print(f"Database {engine.url.database} already exists.")


app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)


with app.app_context():
    db.create_all()


def create_user_if_not_exists(first_name: str, last_name: str, email: str, phone: str, age: int):
    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            age=age,
            signup_date=datetime.datetime.now()
        )
        db.session.add(user)
        db.session.commit()
    print(f'Created user {user}')
    return user


@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@app.route('/users/<uuid:user_id>', methods=['GET'])
def get_user(user_id: uuid.UUID):
    user = User.query.get(str(user_id))
    return jsonify(user.to_dict())


@app.route('/orders/<uuid:user_id>', methods=['GET'])
def get_orders(user_id: uuid.UUID):
    orders = Order.query.filter_by(user_id=str(user_id)).all()
    return jsonify([order.to_dict() for order in orders])


@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

'''
first_name: str, last_name: str, email: str, phone: str,
age: int, quantity: int, color: str, is_tee: bool, 
is_tank: bool, is_hoodie: bool, is_polo: bool, is_hat: bool, 
is_bag: bool, is_other: bool, is_front: bool, is_back: bool, 
is_sleeve: bool, is_tag: bool, garment_quality: int, 
has_artwork: bool, is_hard_deadline: bool, completion_date: str
'''
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'email', 'phone', 'age', 'quantity', 'color', 'is_tee', 'is_tank', 'is_hoodie', 'is_polo', 'is_hat', 'is_bag', 'is_other', 'is_front', 'is_back', 'is_sleeve', 'is_tag', 'garment_quality', 'has_artwork', 'is_hard_deadline', 'completion_date']
    if not data or not all(field in data for field in required_fields):
        return 'Missing required fields', 400
    user = create_user_if_not_exists(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], phone=data['phone'], age=data['age'])

    new_order = Order(
        user_id=user.id,
        quantity=data['quantity'],
        color=data['color'],
        is_tee=data['is_tee'],
        is_tank=data['is_tank'],
        is_hoodie=data['is_hoodie'],
        is_polo=data['is_polo'],
        is_hat=data['is_hat'],
        is_bag=data['is_bag'],
        is_other=data['is_other'],
        is_front=data['is_front'],
        is_back=data['is_back'],
        is_sleeve=data['is_sleeve'],
        is_tag=data['is_tag'],
        garment_quality=data['garment_quality'],
        has_artwork=data['has_artwork'],
        is_hard_deadline=data['is_hard_deadline'],
        completion_date=datetime.datetime.strptime(data['completion_date'], '%Y-%m-%d') if data['completion_date'] else None,
        order_date=datetime.datetime.now()
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
