import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd='Password_Root',
  database = "PyDB_Demo"
)


mycursor = mydb.cursor()


data = [
    ("John", "White", "whiteman@hotmail.com", "UX/UI", "2019-11-09", 36000),
    ("Mary", "Brown", "brownlady@gmail.com", "Full Stack Dev", "2017-10-07", 74000),
    ("Randy", "Armstrong", "randywwe_1995@gmail.com", "Admin", "2015-09-30", 51000),
    ("Kyle", "Smith", "smithy@gmail.com", "Full Stack Dev", "2019-07-21", 69000),
    ("Micheal", "Nackson", "the_real_micheal@gmail.com", "Office Manager", "2016-01-23", 65000) 
    ]

stmt = "INSERT INTO employees (first_name, last_name, email, Job_Title, Hire_Date, Salary) VALUES ('%s','%s','%s','%s','%s','%s')"

mycursor.executemany(stmt,data)


mydb.commit()


print(mycursor.rowcount, 'row(s) inserted')
print('------------------')
print('result with labels:')
print('------------------')

mycursor.execute('SELECT * FROM employees')

for record in mycursor:
    print('Emp ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title', record[4])
    print('Hire Date', record[5])
    print('Salary', record[6])
    print('**********************************')
