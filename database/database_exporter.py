#!/bin/python3

import mysql.connector as con
import os

connection = con.connect(host='localhost', user='root', db='data_science')
cursor = connection.cursor()

table_name = input("Enter table name: ")
file_path = input("Enter csv file path: ")

cursor.execute(f"DESCRIBE {table_name}")
meta_data = []
for entry in cursor.fetchall():
    meta_data.append(entry[0])

cursor.execute(f"SELECT * FROM {table_name}")
file = open(file_path, 'w')
file.write(f'{",".join(meta_data)}{os.linesep}')
for data in cursor.fetchall():
    file.write(f'{",".join(data)}{os.linesep}')
file.close()