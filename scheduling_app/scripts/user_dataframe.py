from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from crm_app.models import Order, User, db


DATABASE_URL = 'postgresql://postgres:postgres@db:5432/crm'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

results = session.query(User, Order).join(Order).all()

user_keys = User.__table__.columns.keys()
new_user_keys = [f'user_{key}' for key in user_keys]
order_keys = Order.__table__.columns.keys()
new_order_keys = [f'order_{key}' for key in order_keys]


data = []
for user, order in results:
    new_item = {}
    for (key, new_key) in zip(user_keys, new_user_keys):
        new_item[new_key] = getattr(user, key)
    for (key, new_key) in zip(order_keys, new_order_keys):
        new_item[new_key] = getattr(order, key)
    data.append(new_item)

df = pd.DataFrame(data)

# save the dataframe to a csv file
df.to_csv('/opt/airflow/data/user_dataframe.csv', index=False)


session.close()
