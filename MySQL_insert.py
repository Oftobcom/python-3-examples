import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO t_python (nom, shahr) VALUES (%s, %s)"
val = ("John", "Конибодом")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
