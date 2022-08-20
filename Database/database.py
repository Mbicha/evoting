import mysql.connector as myconn

myConfig = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'evoting'
}

connection = myconn.connect(**myConfig)

cursor = connection.cursor()
