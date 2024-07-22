import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../crm_app')))

# Replace with valid credentials or automate with email API
GOOGLE_EMAIL_ID = "1234567@email.com"
GOOGLE_APP_PASSWORD = "abcdefghijklmnop"

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import random
import smtplib
from email.mime.text import MIMEText

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

def send_promo_codes():
    # load emails from prioritized_user_emails.txt
    with open('/opt/airflow/data/prioritize_user_emails.txt', 'r') as f:
        emails = f.readlines()
    emails = [email.strip() for email in emails]
    # users = User.query.filter(User.signup_date >= datetime.now() - timedelta(days=30)).filter(User.first_name == 'Bob').all()
    for email in emails:
        promo_code = f'PROMO-{random.randint(1000, 9999)}'
        send_email(email, promo_code)

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

t4 = BashOperator(
    task_id='print_path',
    bash_command='ls /opt/airflow',
    dag=dag,
)

t1 = BashOperator(
    task_id='create_user_dataframe',
    bash_command='python /opt/airflow/scripts/user_dataframe.py',
    dag=dag,
)

t2 = BashOperator(
    task_id='process_user_features',
    bash_command='python /opt/airflow/scripts/process_user_features.py',
    dag=dag,
)

t3 = PythonOperator(
    task_id='send_promo_codes',
    python_callable=send_promo_codes,
    dag=dag,
)


t4 >> t1 >> t2 >> t3