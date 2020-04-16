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

items = [{'name': 'inch', 'price' : 2000},
         {'name': 'nine', 'price' : 3000},
         {'name': 'nails', 'price' : 4000},
         {'name': 'vest', 'price' : 5000},
         {'name': 'gun', 'price' : 6000},
         {'name': 'table', 'price' : 7000}]

class Item(Resource):
    #@jwt_required()
    def get(self, name):
        item = next(filter(lambda i: i['name'] == name, items), None)
        return {'item':item}, 200 if item else 404
     
    def post(self, name):
        if(next(filter(lambda i: i['name'] == name, items), None) is not None):
            return {'message': 'item named {} already exists'.format(name)}, 400
        data = request.get_json(force=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda i: i['name'] != name, items))
        return {'message': 'item deleted'}
    
    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda i: i['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
           
        return item
            
   
class ItemList(Resource):
    def get(self):
        return {'items': items}   
    

     
       
        
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000) 