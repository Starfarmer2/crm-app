import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from crm_app.models import db, User
from explore_data.fake_credentials import GOOGLE_EMAIL_ID, GOOGLE_APP_PASSWORD
import random
import smtplib
from email.mime.text import MIMEText

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def send_promo_codes():
    with app.app_context():
        users = User.query.filter(User.signup_date >= datetime.now() - timedelta(days=30)).filter(User.first_name == 'Bob').all()
        for user in users:
            promo_code = f'PROMO-{random.randint(1000, 9999)}'
            send_email(user.email, promo_code)

def send_email(to_email, promo_code):
    msg = MIMEText(f'Here is your promo code: {123}')
    msg['Subject'] = 'Your Promo Code'
    msg['From'] = GOOGLE_EMAIL_ID
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(GOOGLE_EMAIL_ID, GOOGLE_APP_PASSWORD)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

dag = DAG(
    'send_promo_codes',
    default_args=default_args,
    description='Send promo codes to new users',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

t1 = PythonOperator(
    task_id='send_promo_codes',
    python_callable=send_promo_codes,
    dag=dag,
)
