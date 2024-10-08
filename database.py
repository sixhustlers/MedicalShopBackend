import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='nihal',
    password='temppass',
    database='noteapp'
)

mydb.autocommit=True
pool=mydb.cursor(dictionary=True)