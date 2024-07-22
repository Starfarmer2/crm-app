#https://stackoverflow.com/questions/72478573/how-to-send-an-email-using-python-after-googles-policy-update-on-not-allowing-j

import smtplib
from email.mime.text import MIMEText
from credentials import GOOGLE_EMAIL_ID, GOOGLE_APP_PASSWORD

msg = MIMEText(f'Here is your promo code: {123}')
msg['Subject'] = 'Your Promo Code'
msg['From'] = GOOGLE_EMAIL_ID
msg['To'] = 'wenjia.hu@duke.edu'

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(GOOGLE_EMAIL_ID, GOOGLE_APP_PASSWORD)
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
