#importing required libraries to the app
import requests

#the main redirection
request = requests.get('http://127.0.0.1:8000')
print(request.json())
