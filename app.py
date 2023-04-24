from db_operations import *

# Main
def main():
    conn = connect_database()
    cursor = conn.cursor()


    cursor.close()
    conn.close()