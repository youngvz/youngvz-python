from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

global count
count = 0

""" This route is answers to the GET requests and returns back a welcome string """
@app.route("/")
def welcome():
    return 'Welcome to the Flask Server'

""" This route is answers to the POST requests and returns back a greeting string """
@app.route("/greet", methods=['POST'])
def greet():
    return jsonify('Hi Viraj')


""" This route is answers to the GET requests and returns back the count """
@app.route("/count", methods=['GET'])
def getCount():
    return jsonify({'count': count})

""" This route is answers to the POST requests and increments the count """
@app.route("/count", methods=['POST'])
def increment():
    global count
    count += 1
    return jsonify({'count': count})

""" This route is answers to the POST requests and resets the count """
@app.route("/reset", methods=['POST'])
def reset():
    global count
    count = 0
    return jsonify({'count': count})