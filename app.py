from db_operations import *
import db_operations as db

def display_table(conn, tablename):
    db.pretty_print_table(conn, tablename)

def display_user_table (conn, user_id, tablename):
    db.display_user_table(conn, user_id, tablename)

def create_a_budget(conn, user_id):
    pretty_print_table(conn, 'budgets')
    pretty_print_table(conn, 'categories')


# Main
def main():
    conn = connect_database()
    cursor = conn.cursor()
    print("Welcome to the Credit Application Database")

    # Test
    display_user_table(conn, 2, 'Transactions')
    create_a_budget(conn, 2)

    #import_transactions(conn)
    cursor.close()
    conn.close()

main()