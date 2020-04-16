'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Employee(Resource):
    def get(self, name, pay):
        return {'employee': name, 'salary': pay}

       
        
api.add_resource(Employee, '/employee/<string:name>/<string:pay>')
app.run(port=5000) 