from flask import Flask, url_for, redirect, render_template, request
import urllib
import json

app = Flask(__name__)

# json_url = urllib.urlopen(urltag)
# data = json.loads(json_url.read())
# # print(data)

# r = request.get(urltag)
# print(r.json())

# def get_bio(username):
#     data = request.get_json()
#     bio_data = data.get('bio')
#     print(bio_data)

url = "/github.com/users/"
Username = input("Username: ")
urltag = url+Username
print(urltag)

@app.route(urltag,methods=['GET'])
def proxy_example():
    r = request.get(urltag)
    data = r.json()
    bio = data.get('bio')
    print(bio)
 

if __name__ == "__main__":
    app.run(debug=True)

