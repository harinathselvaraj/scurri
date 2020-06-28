'''
Name: test_app.py
Author: Harinath Selvaraj
Date: 27 June 2020
Version: 1.00
Description: Test cases for the flask web application to validate UK postal codes
'''

# Testing UK Postal code validator script
from app import index, uk_postal_code_validator

# general test
def test_index():
    assert index() == "Hello, world!"

# Input - 'DUMMY'
def test_validator_1(): 
    assert uk_postal_code_validator('DUMMY') == "N"

# Input - 'SW1W 0NY'
def test_validator_2():
    assert uk_postal_code_validator('SW1W 0NY') == "Y"

# Check Small cases
def test_validator_3():
    assert uk_postal_code_validator('sw1w 0ny') == "N"

# Input - 'ASCN 1ZZ'
def test_validator_4():
    assert uk_postal_code_validator('ASCN 1ZZ') == "Y"

# Input - 'L1 8JQ'
def test_validator_5():
    assert uk_postal_code_validator('L1 8JQ') == "Y"

# Input - 'ABC DEF'
def test_validator_6():
    assert uk_postal_code_validator('ABC DEF') == "N"

# Input - 'GU16 7HF'
def test_validator_7():
    assert uk_postal_code_validator('GU16 7HF') == "Y"

# Empty String: Input - ''
def test_validator_8():
    assert uk_postal_code_validator('') == "N"

# Input with Spaces: Input - ' '
def test_validator_9(): # spaces
    assert uk_postal_code_validator(' ') == "N"

# Testing in Frontend
# navigate to project folder in terminal and enter the below,
# python3 app.py
# Navigate to the below URL to check the output.
# http://localhost:1234
# http://localhost:1234/api/?code=SW1W%200NY
# Note: Use %20 instead of a space