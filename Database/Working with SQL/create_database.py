import mysql.connector
mydb = mysql.connector.connect(    # it is creating connection
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor() # upto this it is used for any database creating
mycursor.execute("CREATE DATABASE if not exists test2")
mydb.close()  # to close the connection