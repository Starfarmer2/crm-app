import requests
import json

url = 'http://localhost:5001/users'
response = requests.get(url)

data = json.loads(response.content)
print(json.dumps(data, indent=2))