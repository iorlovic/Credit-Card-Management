
# # Lily 
# import mysql.connector

# # make connection
# conn = mysql.connector.connect(host = "localhost", 
#                                user = "root",
#                                password = "cpsc408!",
#                                auth_plugin = 'mysql_native_password',
#                                database = "CreditApp")

# # create cursor object
# cur_obj = conn.cursor()

# # create database schema
# print("Creating database schema...")
# cur_obj.execute("CREATE SCHEMA CreditApp;")

# cur_obj.execute("USE RideShare;")   # should say 'Database Changed' ???