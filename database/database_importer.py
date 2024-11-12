#!/bin/python3

import mysql.connector as con

connection = con.connect(host='localhost', user='root', db='data_science')
cursor = connection.cursor()

table_name = input("Enter table name: ")
file_path = input("Enter csv file path: ")

def to_snake_case(element:str):
    result = ""
    if element.isupper():
        return element.lower()
    for index, char in enumerate(element):
        if char.isupper() and index > 0:
            result += "_"
        result += char.lower()
    return result

def get_query(file_path:str, table_name:str):
    file = open(file_path)
    first_line = file.readline()
    column_names = [to_snake_case(element.strip()) for element in first_line.split(',')]
    max_length = [0 for _ in column_names]
    data_queries = []
    data_collector = []
    counter = 0
    for line in file:
        line = line.strip()
        if len(line) > 0:
            elements = []
            for index, element in enumerate(line.split(",")):
                element = element.strip()
                elements.append(element)
                if len(element) > max_length[index]:
                    max_length[index] = len(element)
            data_collector.append(",".join(f'"{element}"' for element in elements))
            counter += 1
            if counter == 10:
                aggregated_data = ",".join([f"({data})" for data in data_collector])
                data_queries.append(f"INSERT INTO {table_name} VALUES{aggregated_data}")
                counter = 0
    table_def = ','.join([f'{name} varchar({size})' for name, size in zip(column_names, max_length)])
    file.close()
    return (f"CREATE TABLE IF NOT EXISTS {table_name}({table_def})", data_queries)

table_query, data_queries= get_query(file_path, table_name)

cursor.execute(table_query)
for data_query in data_queries:
    cursor.execute(data_query)
connection.commit()

cursor.close()
connection.close()
