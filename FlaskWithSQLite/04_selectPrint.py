'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

select = "SELECT * FROM users"
for row in cursor.execute(select):
    print(row)

connection.commit()

connection.close()