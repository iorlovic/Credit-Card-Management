CREATE DATABASE creditapp;
USE creditapp;

CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50) -- Increase the length to accommodate longer email addresses
);

CREATE TABLE Credit_Cards (
    card_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    user_id INT,
    card_provider VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES User(user_id) -- Add foreign key constraint
);

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    card_id INT,
    user_id INT,
    amount DECIMAL(10, 2), -- Use DECIMAL type for better precision in monetary values
    merchant VARCHAR(200),
    category_id INT,
    date TIMESTAMP,
    FOREIGN KEY (card_id) REFERENCES Credit_Cards(card_id), -- Add foreign key constraint
    FOREIGN KEY (user_id) REFERENCES User(user_id) -- Add foreign key constraint
);

CREATE TABLE Budgets (
    budget_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    budget_period YEAR,
    budget_amount DECIMAL(10, 2), -- Use DECIMAL type for better precision in monetary values
    FOREIGN KEY (user_id) REFERENCES User(user_id), -- Add foreign key constraint
    FOREIGN KEY (category_id) REFERENCES Categories(categories_id) -- Add foreign key constraint
    UNIQUE (user_id, category_id) -- Add unique constraint for user and category
);

CREATE TABLE Categories (
    categories_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    category VARCHAR(20),
    description VARCHAR(80)
);
