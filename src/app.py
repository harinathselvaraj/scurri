'''
Name: app.py
Author: Harinath Selvaraj
Date: 27 June 2020
Version: 1.00
Description: Flask application that calls module - uk_postal_code_validator.py to 
validate the format of UK postal codes
Usage: Navigate to the currrent folder in terminal and type 'python3 app.py'
        Go to the below URL to check the output.
        http://localhost:1234
        http://localhost:1234/api/?code=SW1W%200NY
        Note: Use %20 instead of a space
'''

import json
from flask import Flask, request
from requests import put, get
from flask_restful import reqparse
from uk_postal_code_validator import uk_postal_code_validator as uk_postal_code_validator

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('code', type=str)

@app.route('/api/', methods=['GET'])
def get():
    args =  request.args
    code = args['code']
    return uk_postal_code_validator(code)

if __name__ == "__main__":
    app.run(port=1234)