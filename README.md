# Credit Card Application and Budget Tracker
Problem/Issue we are trying to resolve
As many have probably experienced as college students transitioning into the adult world, it's hard to track finances and set budgets. Keeping track of multiple credit cards, paying off student loans, monitoring spending habits, and tracking disposable income can be overwhelming. With numerous banking and budgeting apps available, it can be challenging to effectively manage all financial aspects in one place.

Our Solution to the Problem
We created a Database application for users with supported credit card companies, where users will be able to view their financial statements that include their spending habits and transactions, customizable budgets, and a breakdown of user's spending categories.

App Features
Will allow users who have logged in to upload their financial statements from a variety of credit card companies. They will be able to interact and view their financial reports, as well as set a budget for spending. Additionally, users will be able to insert, delete, update, and query transaction data customized to user accounts. Our front-end consists of the user interactive component of the application, developed using HTML and CSS. For our back-end, we will be connecting Python with MySQL.


## Identifying Information

* Name: Ivan Orlovic, Tor Parawell, Lily Annen, and Cal Hegstrom
* Course: CPSC 408
* Assignment: Final Project

## Source Files  
* styles.css
* bargraph.html
* dashboard.html
* login.html
* navbar.html
* pichart.html
* profile.html
* transactionhis.html
* app.py
* README.md

## References

* In class notes and lecture 
* previous assignments
* Ivan took a UI class last semester
* geekforgeeks
* chatgpt for sample data and helping with errors


## Functionalities
List of Functionality:
- Create user graphs from transactions
    - COMPLETED: Pie chart of transactions by category (bar chart, pie chart)
    - COMPLETED: Bar chart of budget vs. transaction amount for a period
- Create a user budget
- Create a new user/card/transaction/etc.
- Search for a transaction by (date (monthly period), name, sort by amount, category, etc)
- Print transactions by category_id
- Add, edit, and delete data. aka financial statments 
- add more tables... (budget table, transaction history, pie chart)
- incorporate login using user email and user_id

## Known Errors

* Is not connected to backend, mysql

## More notes
* for the import csv function, csv_standardize.py allows user to be able to upload raw amex data, and it formats it correctly.


## Build Insructions 
* python app.py

## Execution Instructions
* python app.py
* open the browser it is running on: it should tell you, for us it was: "http://127.0.0.1:5000"