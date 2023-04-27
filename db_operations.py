import os
import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import csv
from datetime import datetime

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

# This function prints a SQL table given a user id and table name
def display_user_table (conn, user_id, tablename):
    column_names = get_column_names(conn, tablename)
    data_query = f"SELECT * FROM {tablename} WHERE user_id = {user_id}"
    data = execute_read_query(conn, data_query)
    
    if column_names and data:
        table = PrettyTable()
        table.field_names = column_names
        for row in data:
            table.add_row(row)
        print(table)
    else:
        print(f"No data found for table {tablename}")

def import_transactions(conn):
    file_path = input("Enter the path to the CSV file: ")

    if os.path.exists(file_path):
        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # Ask the user for the missing data
            pretty_print_table(conn, 'Credit_Cards')
            card_id = input("Enter the card ID for this record: ")
            pretty_print_table(conn, 'User')
            user_id = input("Enter the user ID for this record: ")    
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Extract the data from the CSV row
                date = row['Date']
                merchant = row['Merchant']
                amount = row['Amount']
                category_name = row['Category'].split('-')[0].strip()

                if len(category_name) > 15:
                    print(f"Warning: Category name '{category_name}' is longer than 15 characters.")
                # Get the category_id from the Category table using the category name
                get_category_id_query = "SELECT categories_id FROM Categories WHERE category = %s"
                cursor.execute(get_category_id_query, (category_name,))
                result = cursor.fetchone()

                # Make the datetime format to be compatible with MySQL
                date_obj = datetime.strptime(date, '%m/%d/%y') # Convert to datetime object
                formatted_date = date_obj.strftime('%Y-%m-%d') # Convert to MySQL compatible format
                if result:
                    category_id = result[0]
                else:
                    print(f"Category '{category_name}' not found in the Category table. We will add it as a new category.")
                    # add new category to Categories table
                    add_category_query = "INSERT INTO Categories (category) VALUES (%s)"
                    cursor.execute(add_category_query, (category_name,))
                    conn.commit()
                    # get the new category_id
                    cursor.execute(get_category_id_query, (category_name,))
                    result = cursor.fetchone()
                    category_id = result[0]

                # Prepare the SQL query for inserting the data into the Transactions table
                query = f"""INSERT INTO Transactions (card_id, user_id, amount, merchant, category_id, date)
                            VALUES (%s, %s, %s, %s, %s, %s)"""

                # Execute the query and insert the data
                cursor.execute(query, (card_id, user_id, amount, merchant, category_id, formatted_date))

        # Commit the transaction
        conn.commit()

        # Close the cursor
        cursor.close()

    else:
        print("File not found. Please enter a valid file path.")
