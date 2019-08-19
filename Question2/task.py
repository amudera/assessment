import flask
from flask import Flask, request, jsonify,  url_for, redirect, render_template
import json
import os
from pprint import pprint

app = Flask(__name__)

arr = {'data': [[1,2,3],[4,5,6],[7,8,9]]}

@app.route('/sum', methods=['GET'])
def root():
    arr2 = arr['data']
    vals = sum(map(sum,arr2)) 
    return "Sum: "+str(vals)

# @app.route("/sum", methods=["POST"])
# def json():
#     data = request.get_json()
#     vals = data.get('data')
#     sums = sum(map(sum,vals)) 
#     return jsonify(sums)

# curl localhost:5000/sum/ -d {'data': [[1,2,3],[4,5,6],[7,8,9]]}
# curl -H "Content-Type: application/sum" -X POST -d '{'data': [[1,2,3],[4,5,6],[7,8,9]]}' http://127.0.0.1:5000/

# @app.route("/sum", methods=["POST"])
# def jsondata():
#     arr = {'data': [[1,2,3],[4,5,6],[7,8,9]]}
#     arr2 = request.form.get('data')
#     vals = sum(map(sum,arr2)) 
#     return jsonify(vals)


if __name__ == "__main__":
    app.run(debug=True)