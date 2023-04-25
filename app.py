from db_operations import *
import db_operations as db

# Main
def main():
    conn = connect_database()
    cursor = conn.cursor()
    
    db.pretty_print_table(conn, 'Transactions')

    cursor.close()
    conn.close()

main()