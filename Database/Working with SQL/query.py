import mysql.connector
mydb = mysql.connector.connect(    # it is creating connection
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor() # upto this it is used for any database creating
# mycursor.execute("select * from test2.test_table") # to see the all colume data
mycursor.execute("select c1 , c5 from test2.test_table")  # to see the specific colume data
for i in mycursor.fetchall() :
    print(i)
mydb.close()  # to close the connection