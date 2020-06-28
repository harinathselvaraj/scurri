# Scurri Project

### 1) Tell us about one thing you are proud of in your career. It could be a difficult technical problem you had to solve in your work or a personal project. There is no need to go into details; a short paragraph explaining the problem and why you are proud of it would be fine. 
Answer: I've designed and developed an enterprise level solution to process terabytes of data from different sources including IoT devices in to AWS s3 (file system); process it using Apache Spark and load it in to analytical tables and Implemented best practices to make the front-end and back-end applications scalable using Docker & Kubernetes. I feel proud about it since I was able to architect the whole system in AWS cloud and lead an entire team of 10 members including developers, testers and analysts.

### 2) Question: Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.
Answer: The code is in src/print_numbers/print_numbers.py. The corresponding test cases are in tests/print_numbers/test_print_numbers.py

### 3) Question: Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting. The API that this library provides is your choice.
Answer: The code is in 'src' folder. The corresponding test cases are in tests/app/test_app.py

### Manual Testing
```
git clone https://github.com/harinathselvaraj/scurri
cd path/to/project/folder
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd src

# Testing Flask application to validate UK postal codes
python3 app.py
Notes:
    Go to the below URL to check the output.
    http://localhost:1234
    http://localhost:1234/api/?code=SW1W%200NY
    Note: Use %20 instead of a space

# Running Test Cases for both the projects
cd ../../          #Go back to base folder
pytest

```
### Continous Integration Testing
```
git clone https://github.com/harinathselvaraj/scurri
cd path/to/project/folder
make any simple change to the files. eg) A small change to readme.md
git commit -m "changes to readme.md"
git push
```

Upon code push to github, the server runs the test cases (as per the YAML code given .github/workflows/
python-app.yml). The results of testing can be found under 'Actions'. 