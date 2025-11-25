import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="broadridge"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("Ria", "ria@gmail.com")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")