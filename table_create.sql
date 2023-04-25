CREATE DATABASE creditapp;
USE creditapp;

CREATE TABLE User (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(20)
);

CREATE TABLE Credit_Cards (
    card_id INT PRIMARY KEY,
    user_id INT,
    card_provider VARCHAR(20)
);

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    card_id INT,
    user_id INT,
    amount NUMERIC,
    merchant VARCHAR(40),
    category_id INT,
    date TIMESTAMP
);

CREATE TABLE Budgets (
    budget_id INT PRIMARY KEY,
    user_id INT,
    category_id INT,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    budget_period YEAR,
    budget_amount NUMERIC
);

CREATE TABLE Categories (
    categories_id INT PRIMARY KEY,
    category VARCHAR(20),
    description VARCHAR(80)
);
