from faker import Faker
from models import db, User
from app import app
import datetime

fake = Faker()

def create_fake_users(n):
    for _ in range(n):
        user = User(
            name=fake.name(),
            email=fake.email(),
            age=fake.random_int(min=18, max=80),
            signup_date=fake.date_time_this_decade()
        )
        db.session.add(user)
    db.session.commit()

with app.app_context():
    db.create_all()
    create_fake_users(100)
