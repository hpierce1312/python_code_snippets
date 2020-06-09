import mysql.connector
import csv

connection = mysql.connector.connect(host='localhost', user='root', password='', database='bus443')
cursor = connection.cursor()

cursor.execute("INSERT INTO Faculty (firstname, lastname, coursename, courselocation) VALUES ('Billy', 'Bob', 'BUS 443', 'Online')")
connection.commit()

cursor.execute("SELECT * FROM Faculty")
result = cursor.fetchall()

openfile = open('testcsvfile.csv', 'w', newline='')
csvfile = csv.writer(openfile)
csvfile.writerows(result)

print(result)

openfile.close()
connection.close()
cursor.close()