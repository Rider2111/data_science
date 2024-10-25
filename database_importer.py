import mysql.connector as con

connection = con.connect(host='localhost', user='root')

cursor = connection.cursor()

database_name = input("Enter database name:")
cursor.execute(f"CREATE DATABASE {database_name}")
file_path = input("Enter csv file path:")
file = open(file_path,'r')
first_line = file.readline()
secon_line = file.readline()
cursor.close()
connection.close()