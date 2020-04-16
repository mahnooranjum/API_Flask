'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from securityFile import authenticate, identity

app = Flask(__name__)
app.secret_key = 'flask'
api = Api(app)


jwt = JWT(app, authenticate, identity)

items = [{'name': 'chair', 'price' : 2000}]

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item':item}, 200 if item else 404
     
    def post(self, name):
        if(next(filter(lambda x: x['name'] == name, items), None) is not None):
            return {'message': 'item named {} already exists'.format(name)}, 400
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