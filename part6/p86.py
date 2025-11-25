import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="broadridge"
)
mycursor = mydb.cursor()
mycursor.execute("select * from customers")
result = mycursor.fetchall()
for i in result:
    print(i)