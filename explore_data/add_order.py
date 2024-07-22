import requests

url = 'http://localhost:5001/orders'
data = {
    'first_name': "Bob", 
    'last_name': "Smith", 
    'email': 'wenjia.hu@duke.edu', 
    'phone': '123-456-7890', 
    'age': 29,
    'quantity': 3, 
    'color': 'blue', 
    'is_tee': True, 
    'is_tank': True, 
    'is_hoodie': True, 
    'is_polo': True, 
    'is_hat': True, 
    'is_bag': True, 
    'is_other':True, 
    'is_front': True, 
    'is_back': True, 
    'is_sleeve': True, 
    'is_tag': True, 
    'garment_quality': 5, 
    'has_artwork': True, 
    'is_hard_deadline': True, 
    'completion_date': '2024-09-30'
}
response = requests.post(url, json=data)