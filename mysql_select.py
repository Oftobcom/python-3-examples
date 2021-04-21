import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM t_python")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
