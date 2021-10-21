from flask import Flask, json

import math

app = Flask(__name__)


@app.route('/')
def default_route():
    return 'Welcome Factorial App'


@app.route('/calculateFact/<int:facNumber>')
def calculateFact(facNumber):
    result = '{"Result",'+ str(math.factorial(facNumber))
	
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response
