import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

mycursor = mydb.cursor()

sql = "UPDATE t_python SET shahr = 'конибодом' WHERE shahr = 'New York'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
