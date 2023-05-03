import os
import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def connect_database():
    try: 
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='cpsc408!',
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

import mysql.connector

# Create a new user
def create_user(conn):
    email = input("Enter user email: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (email, first_name, last_name) VALUES (%s, %s, %s)", (email, first_name, last_name))
    conn.commit()
    print("User created successfully")

# Create a new card
def create_card(conn, user_id):
    card_name = input("Enter card name: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Credit_Cards (user_id, card_provider) VALUES (%s, %s)", (user_id, card_name))
    conn.commit()
    print("Card created successfully")

# Search for a transaction
def search_transactions(conn, user_id):
    search_query = input("Enter search query: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE user_id = %s AND (merchant LIKE %s)", (user_id, f'%{search_query}%'))
    transactions = cursor.fetchall()
    for transaction in transactions:
        print(transaction)

# Print transactions by category_id
def print_transactions_by_category_id(conn, user_id):
    category_id = input("Enter category ID: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE user_id = %s AND category_id = %s", (user_id, category_id))
    transactions = cursor.fetchall()
    for transaction in transactions:
        print(transaction)

# Add a transaction
def add_transaction(conn, user_id):
    merchant = input("Enter merchant name: ")
    amount = float(input("Enter transaction amount: "))
    date = input("Enter transaction date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Transactions (user_id, merchant, amount, date) VALUES (%s, %s, %s, %s)", (user_id, merchant, amount, date))
    conn.commit()
    print("Transaction added successfully")
