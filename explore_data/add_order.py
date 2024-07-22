import requests

url = 'http://localhost:5001/orders'
data = {
    'first_name': "James", 
    'last_name': "Brown", 
    'email': 'james.brown@email.edu', 
    'phone': '123-456-7891', 
    'age': 25,
    'quantity': 5, 
    'color': 'black', 
    'is_tee': False, 
    'is_tank': False, 
    'is_hoodie': False, 
    'is_polo': False, 
    'is_hat': True, 
    'is_bag': False, 
    'is_other':False, 
    'is_front': False, 
    'is_back': False, 
    'is_sleeve': False, 
    'is_tag': False, 
    'garment_quality': 2, 
    'has_artwork': True, 
    'is_hard_deadline': True, 
    'completion_date': '2024-10-30'
}
response = requests.post(url, json=data)