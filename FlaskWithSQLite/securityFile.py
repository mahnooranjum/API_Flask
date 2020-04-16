
'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''
from werkzeug.security import safe_str_cmp
from userFile import User



def authenticate(username, password):
    user = User.searchby_name(username)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    user_id = payload['identity'] 
    return User.searchby_id(user_id)

