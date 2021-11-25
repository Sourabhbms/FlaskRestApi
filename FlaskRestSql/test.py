import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
drop_table = "drop table users"
cursor.execute(drop_table)

create_table = "Create table users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "Insert into users values (?, ?, ?)"
cursor.execute(insert_query,user)

users = [
(2, 'rolf', 'asdf'),
(3, 'anne', 'asdf')
    ]

cursor.executemany(insert_query, users)

select_query= "select * from users"
for row in cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()