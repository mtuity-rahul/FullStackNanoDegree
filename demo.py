import psycopg2
connection = psycopg2.connect('dbname=example user=postgres host=localhost password=myPassword')
cursor = connection.cursor()
cursor.execute('DROP TABLE if exists table2;')
cursor.execute('''CREATE TABLE table2 (id INTEGER PRIMARY KEY,completed BOOLEAN NOT NULL DEFAULT False);''')
cursor.execute('INSERT into table2 (id,completed) VALUES(%s,%s);',(1,True))
cursor.execute('''INSERT into table2 (id,completed)
 VALUES(%(id)s,%(completed)s);''',{'id':2,'completed':False})

cursor.execute('select * from table2;')

result= cursor.fetchall()
print(result)
connection.commit()
connection.close()
cursor.close()
