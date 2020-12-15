import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd='Password_Root'
 
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

print(mycursor)

for db in mycursor:
    print(db)



mycursor.execute("USE PyDB_Demo")

mycursor.execute("CREATE TABLE IF NOT EXISTS employees (EmpId int primary key auto_increment, first_name VARCHAR(40), last_name VARCHAR(40), email VARCHAR(50), Job_Title VARCHAR(40), Hire_Date date, Salary decimal check ( salary >= 15000 AND salary <=50000))")


mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

