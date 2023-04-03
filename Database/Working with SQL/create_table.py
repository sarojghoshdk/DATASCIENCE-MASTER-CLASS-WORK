import mysql.connector
mydb = mysql.connector.connect(    # it is creating connection
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor() # upto this it is used for any database creating
mycursor.execute("CREATE TABLE if not exists test2.test_table(c1 INT , c2 VARCHAR(50) , c3 FLOAT , c4 INT , c5 VARCHAR(30)) ;")
mydb.close()