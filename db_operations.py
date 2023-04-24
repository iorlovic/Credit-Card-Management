# db_operations.py
import mysql.connector

# Connects to mySQL database.
def connect_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cpsc-408",
        auth_plugin='mysql_native_password',
        database='RideShare'
    )
    return conn
    
