from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

""" This route is answers to the GET requests and returns back a welcome string """
@app.route("/")
def welcome():
    return 'Welcome to the Flask Server'

""" This route is answers to the POST requests and returns back a greeting string """
@app.route("/greet", methods=['POST'])
def greet():
    return jsonify('Hi Viraj')