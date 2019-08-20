import urllib3
import json
import requests

url = "https://api.github.com/users/"
Username = input("Username: ")
urltag = url+Username

r = requests.get(urltag)
bio = r.json()["bio"] #or r.json().get('bio)
print(bio)