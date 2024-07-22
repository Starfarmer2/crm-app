# In the crm_app/models.py file, the Order class has a method to_dict that returns a dictionary representation of an Order instance. 
# In the crm_app/app.py file, the app is created with Flask and SQLAlchemy, and routes are defined to retrieve user and order data from the database. 
# The create_user_if_not_exists function creates a new user if one does not already exist in the database. 
# The crm_app/fill_db.py file uses the Faker library to create fake user data and populate the database with it. 
# The airflow_app/scripts/user_dataframe.py script queries the database to retrieve user and order data, combines the data into a single dataframe, and saves the dataframe to a CSV file.

import pandas as pd
import numpy as np
import datetime

# load user_dataframe.csv into a pandas dataframe
df = pd.read_csv('/opt/airflow/data/user_dataframe.csv')

# decay factor for exponential weighting
decay_factor = 0.05

# threshold for decrease in order amount
threshold = 5

now = datetime.datetime.now(datetime.UTC)
now_naive = now.replace(tzinfo=None)
print(now)

prioritize_user_emails = []

for user_email in df['user_email'].unique():
    user_df = df[df['user_email'] == user_email]
    user_df = user_df.sort_values(by='order_order_date')
    user_df['order_order_date'] = pd.to_datetime(user_df['order_order_date'])
    user_df['user_signup_date'] = pd.to_datetime(user_df['user_signup_date'])
    user_df['time_diff_order_signup'] = user_df['order_order_date'] - user_df['user_signup_date']
    user_df['time_diff_now_order'] = now_naive - user_df['order_order_date']

    # convert to days
    user_df['time_diff_order_signup'] = user_df['time_diff_order_signup'].apply(lambda x: x.days)
    user_df['time_diff_now_order'] = user_df['time_diff_now_order'].apply(lambda x: x.days)

    user_df['exp_time_diff_order_signup'] = np.exp(-user_df['time_diff_order_signup'] * decay_factor)
    user_df['exp_time_diff_now_order'] = np.exp(-user_df['time_diff_now_order'] * decay_factor)

    # quantify user's order amount + user's order quality
    user_df['order_total'] = user_df['order_quantity'] * user_df['order_garment_quality']

    avg_order_total = user_df['order_total'].mean()
    exp_weighted_avg_order_total = np.sum(user_df['order_total'] * user_df['exp_time_diff_now_order']) / len(user_df)  # weighted by 1/exp(now - order placement time)

    print(avg_order_total, exp_weighted_avg_order_total)
    if avg_order_total - exp_weighted_avg_order_total >= threshold:
        print(f"User {user_email} has a decrease in order amount")
        prioritize_user_emails.append(user_email)

# save the list of user emails to a text file
with open('/opt/airflow/data/prioritize_user_emails.txt', 'w') as f:
    for email in prioritize_user_emails:
        f.write(f"{email}\n")
