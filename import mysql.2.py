import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "demo_db"
)
mycursor = mydb.cursor()
sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
data = (500, "keerthana")

mycursor.execute(sql, data)
mydb.commit()
print(mycursor.rowcount, "record inserted.")