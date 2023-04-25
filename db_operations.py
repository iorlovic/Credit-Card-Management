import os
import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable

def connect_database():
    try: 
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='cpsc-408',
            auth_plugin='mysql_native_password',
            database='creditapp'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def get_column_names(connection, table_name):
    query = f"SHOW COLUMNS FROM {table_name}"
    result = execute_read_query(connection, query)
    column_names = [row[0] for row in result] if result else []
    return column_names

def pretty_print_table(connection, table_name):
    column_names = get_column_names(connection, table_name)
    data_query = f"SELECT * FROM {table_name}"
    data = execute_read_query(connection, data_query)
    
    if column_names and data:
        table = PrettyTable()
        table.field_names = column_names
        for row in data:
            table.add_row(row)
        print(table)
    else:
        print(f"No data found for table {table_name}")