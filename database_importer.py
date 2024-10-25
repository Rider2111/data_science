import mysql.connector as con

connection = con.connect(host='localhost', user='root', db='data_science')

cursor = connection.cursor()

table_name = input("Enter table name:")

file_path = input("Enter csv file path:")
file = open(file_path,'r')

first_line = file.readline()
column_names = [n.strip() for n in first_line.split(',')]

max_length = []
for _ in first_line.split(","):
    max_length.append(0)
for line in file:
    for index, element in enumerate(line.split(",")):
        if len(element) > max_length[index]:
            max_length[index] = len(element)
print(max_length)

query = f"CREATE TABLE {table_name}("
sub_queries = []
zip_result = zip(column_names, max_length)
for name, size in zip_result:
    sub_query = f"{name} varchar({size})"
    sub_queries.append(sub_query)

query += ','.join(sub_queries)
query += ')'
print(query)
cursor.execute(query)
cursor.close()
connection.close()