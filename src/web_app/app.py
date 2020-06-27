import json
from flask import Flask, request
from requests import put, get
from flask_restful import reqparse
from uk_postal_code_validator import uk_postal_code_validator

app = Flask(__name__)

@app.route('/')
def default():
    return "Hello, world!"

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('code', type=str)

# http://localhost:1234/api/?code=SW1W%200NY

@app.route('/api/', methods=['GET'])
def get():
    args =  request.args
    code = args['code']
    return uk_postal_code_validator(code)

if __name__ == "__main__":
    app.run(port=1234)