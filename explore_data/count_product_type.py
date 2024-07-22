from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../crm_app')))

from ..crm_app.models import Order, User, db


DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/crm'  # Adjust as needed

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Function to count orders of particular product_type
def count_orders_where_true(product_type):
    count = session.query(Order).filter(getattr(Order, product_type) == True).scalar()
    return count

if __name__ == '__main__':
    # product_types = ['is_tee', 'is_tank', 'is_hoodie', 'is_polo', 'is_hat', 'is_bag', 'is_other']
    product_type = 'is_tee'
    total_orders = count_orders_where_true(product_type=product_type)
    print(f"Total number of orders where {product_type} is True: {total_orders}")

# Close the session
session.close()
