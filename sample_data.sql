-- Insert sample data into User table
INSERT INTO User (user_id, first_name, last_name, email)
VALUES (1, 'John', 'Doe', 'john.doe@example.com'),
       (2, 'Jane', 'Smith', 'jane.smith@example.com'),
       (3, 'Michael', 'Brown', 'michael.brown@example.com'),
       (4, 'Emily', 'Johnson', 'emily.johnson@example.com');

-- Insert sample data into Credit_Cards table
INSERT INTO Credit_Cards (card_id, user_id, card_provider)
VALUES (1, 1, 'Visa'),
       (2, 2, 'Mastercard'),
       (3, 3, 'American Express'),
       (4, 4, 'Discover');

-- Insert sample data into Categories table
INSERT INTO Categories (categories_id, category, description)
VALUES (1, 'Groceries', 'Expenses on food and household items'),
       (2, 'Entertainment', 'Expenses on movies, concerts, and other leisure activities'),
       (3, 'Utilities', 'Expenses on electricity, gas, water, and other utilities'),
       (4, 'Restaurants', 'Expenses on dining out and takeout food');

-- Insert sample data into Transactions table
INSERT INTO Transactions (transaction_id, card_id, user_id, amount, merchant, category_id, date)
VALUES (1, 1, 1, 100, 'Supermarket A', 1, '2023-04-01 15:30:00'),
       (2, 1, 1, 50, 'Cinema B', 2, '2023-04-05 20:15:00'),
       (3, 2, 2, 200, 'Supermarket C', 1, '2023-04-10 18:45:00'),
       (4, 3, 3, 75, 'Restaurant D', 4, '2023-04-15 12:30:00'),
       (5, 4, 4, 30, 'Utility Company E', 3, '2023-04-20 10:00:00');

-- Insert sample data into Budgets table
INSERT INTO Budgets (budget_id, user_id, category_id, start_date, end_date, budget_period, budget_amount)
VALUES (1, 1, 1, '2023-04-01 00:00:00', '2023-04-30 23:59:59', '2023', 500),
       (2, 1, 2, '2023-04-01 00:00:00', '2023-04-30 23:59:59', '2023', 200),
       (3, 2, 1, '2023-04-01 00:00:00', '2023-04-30 23:59:59', '2023', 600),
       (4, 3, 3, '2023-04-01 00:00:00', '2023-04-30 23:59:59', '2023', 100),
       (5, 4, 4, '2023-04-01 00:00:00', '2023-04-30 23:59:59', '2023', 300);
