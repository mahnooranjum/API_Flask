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

items = []

class Item(Resource):
    def get(self, name):
        for item in items: 
            if item['name'] == name:
                return item
        return {'message': 'no such item'}, 404       
     
    def post(self, name):
        item = {'name': name, 'price': 16}
        items.append(item)
        return item, 201

       
        
api.add_resource(Item, '/item/<string:name>')
app.run(port=5000) 