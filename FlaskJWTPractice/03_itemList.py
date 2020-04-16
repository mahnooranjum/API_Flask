'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [{'name': 'chair', 'price' : 2000}]

class Item(Resource):
    def get(self, name):
        for item in items: 
            if item['name'] == name:
                return item
        return {'message': 'no such item'}, 404       
     
    def post(self, name):
        data = request.get_json(force=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
class ItemList(Resource):
    def get(self):
        return {'items': items}   
     
       
        
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000) 