'''
    Author:Mahnoor Anjum
    Description:
        Learning the basics of Flask, Hands on!
'''

from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

people = [{'name': 'Joker', 
         'email': 'batmanmustdie@gmail.com', 
         'items': ['Not the bat mobile', 'not a sense of humor']}
        ]

#get /people
@app.route('/')
def home():
  return render_template('index.html')

#get /people
@app.route('/people')
def get_people():
  return jsonify({'people': people})

@app.route('/people/<string:name>')
def get_person(name):
    for i in people:
        if i['name'] == name:
            return jsonify(i)
    return jsonify({"message":"no such person, please create"})

@app.route('/people', methods = ['POST'])
def create_people():
    data = request.get_json()
    for i in people:
        if i['name'] == data['name']:
            return jsonify(i)
        else:
            pass    
    person = {'name': data['name'],
              'email': data['email'],
              'items': []}
    people.append(person)
    return jsonify(person)

@app.route('/people/<string:name>/items')
def get_items(name):
    for i in people:
        if i['name'] == name:
            return jsonify(i['items'])
    return jsonify({"message":"no such person, please create"})

@app.route('/people/<string:name>/items', methods = ['POST'])
def post_items(name):
    data = request.get_json()
    for i in people:
        if i['name'] == name:
            if data['items'] not in i['items']:
                i['items'].append(data['items'])
                return jsonify(i['items'])
            return jsonify({'message': 'item already present'})
    return jsonify({"message":"no such person, please create"})

app.run(port=5000)
