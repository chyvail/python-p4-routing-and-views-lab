#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    result = ""
    for i in range(param):
        result += f"{i}\n"
    return result

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    if (operation == "+"):
        value = int(num1) + int(num2)
        return str(value)
    
    elif (operation == "-"):
        value = int(num1) - int(num2)
        return str(value)
    
    elif (operation == "*"):
        value = int(num1) * int(num2)
        return str(value)
    
    elif (operation == "div"):
        value = int(num1) / int(num2)
        return str(value)
    
    elif (operation == "%"):
        value = int(num1) % int(num2)
        return str(value)
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
