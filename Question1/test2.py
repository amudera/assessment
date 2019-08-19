import urllib3
from flask import Flask, url_for, redirect, render_template, request, Response, session
import json
import requests

url = "https://github.com/users/"
Username = input("Username: ")
urltag = url+Username

r = requests.get(urltag)
bio = r.get("bio")
print(bio)