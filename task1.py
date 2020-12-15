import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd='Password_Root'
 
)

mycursor = mydb.cursor()


mycursor.execute ("CREATE DATABASE PyDB_Demo")


mycursor.execute ("USE  PyDB_Demo")


mycursor.execute("CREATE TABLE employees  (emp_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(40) NOT NULL, last_name VARCHAR(40) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, job_title VARCHAR(40) NOT NULL, date_hired DATE NOT NULL, salary DEC CHECK ( salary >= 15000 AND salary <= 50000) ))")


mycursor.execute("SHOW TABLES")
for table in mycursor:
  print(table)
