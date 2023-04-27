from db_operations import *
import db_operations as db

def display_table(conn, tablename):
    db.pretty_print_table(conn, tablename)

def display_user_table (conn, user_id, tablename):
    db.display_user_table(conn, user_id, tablename)


# Another possibly for a budget SCHEMA
'''
CREATE TABLE Budgets (
    budget_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    user_id INT,
    category_id INT,
    budget_frequency ENUM('monthly', 'quarterly', 'yearly'),
    budget_amount DECIMAL(10, 2), -- Use DECIMAL type for better precision in monetary values
    FOREIGN KEY (user_id) REFERENCES User(user_id), -- Add foreign key constraint
    FOREIGN KEY (category_id) REFERENCES Categories(categories_id), -- Add foreign key constraint
    UNIQUE (user_id, category_id) -- Add unique constraint for user and category
);
'''
def create_a_budget(conn, user_id):
    print("Here are your current budget and amounts")
    db.display_user_table(conn, user_id, "Budgets")

    display_table(conn, "Categories")
    category_id = input("Enter a category id for your budget: ")
    budget_amount = input("Enter a budget amount: ")

    start_date = input("Enter the start date for your budget (YYYY-MM-DD): ")
    end_date = input("Enter the end date for your budget (YYYY-MM-DD): ")
    budget_period = input("Enter the budget period (YYYY): ")

    budget_query = f"INSERT INTO Budgets (user_id, category_id, start_date, end_date, budget_period, budget_amount) VALUES ({user_id}, {category_id}, '{start_date}', '{end_date}', '{budget_period}', {budget_amount})"
    db.execute_query(conn, budget_query)

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