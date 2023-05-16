# Authors: Tor Parawell
from db_operations import *
import db_operations as db
def display_table(conn, tablename):
    db.pretty_print_table(conn, tablename)

def display_user_table (conn, user_id, tablename):
    db.display_user_table(conn, user_id, tablename)

def create_a_budget(conn, user_id):
    print("Here are your current budget and amounts")
    display_user_table(conn, user_id, "Budgets")

    display_table(conn, "Categories")
    category_id = input("Enter a category id for your budget: ")
    budget_amount = input("Enter a budget amount: ")

    start_date = input("Enter the start date for your budget (YYYY-MM-DD): ")
    end_date = input("Enter the end date for your budget (YYYY-MM-DD): ")
    budget_period = input("Enter the budget period (YYYY): ")

    budget_query = f"INSERT INTO Budgets (user_id, category_id, start_date, end_date, budget_period, budget_amount) VALUES ({user_id}, {category_id}, '{start_date}', '{end_date}', '{budget_period}', {budget_amount})"
    execute_query(conn, budget_query)

def get_budget_and_spending(conn, user_id):
    cursor = conn.cursor()

    # Get total budget amounts for each category for the user
    cursor.execute("""
        SELECT c.category, SUM(b.budget_amount) as total_budget
        FROM Budgets b
        JOIN Categories c ON b.category_id = c.categories_id
        WHERE b.user_id = %s
        GROUP BY c.category
    """, (user_id,))
    budgets = cursor.fetchall()
    print(budgets)
    # Get total spending amounts for each category for the user
    cursor.execute("""
        SELECT c.category, SUM(t.amount) as total_spending
        FROM Transactions t
        JOIN Categories c ON t.category_id = c.categories_id
        WHERE t.user_id = %s
        GROUP BY c.category
    """, (user_id,))
    spendings = cursor.fetchall()

    # Combine budget and spending data
    budget_spending = {}
    for category, total_budget in budgets:
        budget_spending[category] = {"total_budget": total_budget, "total_spending": 0}

    for category, total_spending in spendings:
        if category in budget_spending:
            budget_spending[category]["total_spending"] = total_spending

    return budget_spending


def budget_vs_spending_graph(conn, user_id):
    # Fetch budget and spending data
    budget_spending = get_budget_and_spending(conn, user_id)

    # Prepare data for visualization
    categories = list(budget_spending.keys())
    budget_data = [x["total_budget"] for x in budget_spending.values()]
    spending_data = [x["total_spending"] for x in budget_spending.values()]

    # Create a bar chart
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(categories))

    ax.bar(index, budget_data, bar_width, label="Budget")
    ax.bar(index + bar_width, spending_data, bar_width, label="Spending")

    # Set chart labels and title
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
    ax.set_title("Budget vs. Spending")
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(categories)
    ax.legend()

    # Display the graph
    plt.show()

def get_transactions_by_category(conn, user_id):
    cursor = conn.cursor()

    # Get the sum of transaction amounts for each category for the given user_id
    cursor.execute("""
        SELECT c.category, SUM(t.amount) as total_amount
        FROM Transactions t
        JOIN Categories c ON t.category_id = c.categories_id
        WHERE t.user_id = %s
        GROUP BY c.category
    """, (user_id,))
    transactions = cursor.fetchall()

    return transactions

def transactions_by_category_pie_chart(conn, user_id):
    # Fetch transaction data grouped by category
    transactions_by_category = get_transactions_by_category(conn, user_id)

    # Prepare data for visualization
    categories = [x[0] for x in transactions_by_category]
    transaction_amounts = [x[1] for x in transactions_by_category]

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(transaction_amounts, labels=categories, autopct='%1.1f%%', startangle=90)

    # Set the title
    ax.set_title("Transactions by Category")

    # Display the pie chart
    plt.show()

def delete_transactions(conn, user_id):
    display_user_table(conn, user_id, "Transactions")
    transaction_id = input("Enter the transaction id to delete: ")
    db.delete_transaction(conn, user_id, transaction_id)

def print_menu():
    print("\nWelcome to the Credit Application Database")
    print("Choose an option:")
    print("1. Import transactions from CSV")
    print("2. Create a budget")
    print("3. Display transactions by category (Pie chart)")
    print("4. Display budget vs. spending (Bar chart)")
    print("5. Create a new user")
    print("6. Create a new card")
    print("7. Search for a transaction")
    print("8. Print transactions by category_id")
    print("9. Add a financial statement")
    print("10. Print SQL tables")
    print("11. Delete a transaction")
    print("12. Update transactions")
    print("13: Generate reports")
    print("14. Exit")

def main():
    conn = connect_database()
    user_id = 2
    admin_user_report(conn)
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            import_transactions(conn)
        elif choice == 2:
            create_a_budget(conn, user_id)
        elif choice == 3:
            transactions_by_category_pie_chart(conn, user_id)
        elif choice == 4:
            budget_vs_spending_graph(conn, user_id)
        elif choice == 5:
            create_user(conn)
        elif choice == 6:
            create_card(conn, user_id)
        elif choice == 7:
            search_transactions(conn, user_id)
        elif choice == 8:
            print_transactions_by_category_id(conn, user_id)
        elif choice == 9:
            add_transaction(conn, user_id)
        elif choice == 10:
            # Pirnts all of the SQL tables.
            print_table = input("Which table would you like to print? ")
            display_table(conn, print_table)
        elif choice == 11:
            delete_transactions(conn, user_id)
        elif choice == 12:
            transaction_id = input("Enter the transaction ID to be updated: ")
            new_amount = input("Enter the new amount: ")
            update_transaction(conn, user_id, transaction_id, new_amount)
        elif choice == 13:
            db.generate_user_report(conn, user_id)
        elif choice == 14:
            print("Thank you for using the Credit Application Database. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from the available options.")
    conn.close()

if __name__ == "__main__":
    main()