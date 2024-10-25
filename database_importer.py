import mysql.connector as con

connection = con.connect(host='localhost', user='root')

cursor = connection.cursor()

database_name = input("Enter database name:")
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

file_path = input("Enter csv file path:")
file = open(file_path,'r')

first_line = file.readline()

data = []
for _ in first_line.split(","):
    data.append(0)
for line in file:
    for index, element in enumerate(line.split(",")):
        if len(element) > data[index]:
            data[index] = len(element)

cursor.close()
connection.close()