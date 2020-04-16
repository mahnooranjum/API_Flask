'''
    Mahnoor Anjum
    Flask Practice
    Codes inspired by: 
        https://github.com/schoolofcode-me/rest-api-sections
'''

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
user = (1, 'mahnoor', '1234')
insert = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert, user)

users = [(2, 'usman', '123'),
         (3, 'umer', '123'),
         (4, 'joker', '123')]


cursor.executemany(insert, users)
select = "SELECT * FROM users"
for row in cursor.execute(select):
    print(row)

connection.commit()

connection.close()
