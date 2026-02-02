import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "demo"
)

mycursor = mydb.cursor()

# list of 10 records: (id, name, lastname, password)
data = [
    (400, "keerthana", "k", "keerthana@123"),
    (401, "keer", "k", "keer@123"),
    (402, "karthi", "s", "karthi@123"),
    (403, "sathish", "r", "sathish@123"),
    (404, "vijay", "m", "vijay@123"),
    (405, "ajith", "k", "ajith@123"),
    (406, "surya", "s", "surya@123"),
    (407, "dhanush", "k", "dhanush@123"),
    (408, "vicky", "r", "vicky@123"),
    (409, "arun", "k", "arun@123"),
]

sql = "INSERT INTO login (id, name, lastname, password) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sql, data)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

 # Append all rows
for row in data:
    print(row)

alter_sql = "UPDATE login SET password = %s WHERE id = %s"
alter_values = ("keerthana@12", 270)
delete_sql = "DELETE FROM login WHERE id = %s"
delete_value = (273,)
mycursor.execute(alter_sql, alter_values)
mydb.commit()
mycursor.execute(delete_sql, delete_value)
mydb.commit()
print("Record updated and deleted successfully.")