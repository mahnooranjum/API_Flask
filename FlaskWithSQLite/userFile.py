'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''
import sqlite3
from flask_restful import Resource, reqparse
class User():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def searchby_name(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username=?"
        output = cursor.execute(query, (username,))
        match = output.fetchone()
        
        if match is not None:
            user = cls(match[0], match[1], match[2])
            #user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def searchby_id(cls, user_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id=?"
        output = cursor.execute(query, (user_id,))
        match = output.fetchone()
        
        if match is not None:
            user = cls(match[0], match[1], match[2])
            #user = cls(*row)
        else:
            user = None
        connection.close()
        return user
    
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
                        type= str,
                        required = True, 
                        help = "Field can not be empty")
    parser.add_argument('password', 
                    type= str,
                    required = True, 
                    help = "Field can not be empty")
    def post(self):        
        data = UserRegister.parser.parse_args()
        if User.searchby_name(data['username']):
            return {'message': 'username already registered'}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?,?)"
        cursor.execute(query, (data['username'], data['password']))
        
        connection.commit()
        connection.close()
        return {'message': 'user created successfully'}, 201
    
    