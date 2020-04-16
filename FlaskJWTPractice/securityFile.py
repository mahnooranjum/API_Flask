'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''
from werkzeug.security import safe_str_cmp
from userFile import User

users = [User(1, 'mahnoor', '1234'),User(1, 'usman', '1234')]

username_mapping = {i.username: i for i in users}

userid_mapping = {i.id: i for i in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    user_id = payload['identity'] 
    return userid_mapping.get(user_id, None)


'''
users = [{
        'id':1,
        'username': 'mahnoor',
        'password': '1234'
        },
        {
        'id':2,
        'username': 'usman',
        'password': '5678'
        }]

username_mapping = {i['username']: i for i in users}

userid_mapping = {i['id']: i for i in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
'''