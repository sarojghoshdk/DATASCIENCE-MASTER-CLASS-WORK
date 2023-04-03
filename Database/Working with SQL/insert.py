import mysql.connector
mydb = mysql.connector.connect(    # it is creating connection
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor() # upto this it is used for any database creating
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")
mycursor.execute("insert into test2.test_table values(123 , 'saroj' , 254.32 , 582 , 'ghosh')")


mydb.commit()
mydb.close()