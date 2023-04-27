import csv
import os
import re


def extract_merchant_name(input_string):
    # Remove the spaces that have more than 2 spots
    input_string = re.sub(r'\s{2,}', ' ', input_string)

    # Remove the leading and trailing spaces
    input_string = input_string.strip()

    # Remove "AplPay" if it is at the front of the string
    input_string = re.sub(r'^AplPay', '', input_string).strip()

    # Remove State Code from string:
    input_string = re.sub(r'\s[A-Z]{2}$', '', input_string)

    # Remove TST* if it is at the front of the string
    input_string = re.sub(r'^TST\*', '', input_string)
    
    return input_string.strip()

def read_csv():
    input_filename = input("Enter the path to the CSV file: ")
    output_filename = input("Enter the path for the output CSV file: ")

    if os.path.exists(input_filename):
        with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
            reader = csv.DictReader(input_file)

            fieldnames = ['Date', 'Merchant', 'Amount', 'Category', 'Description']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                date = row['Date']
                merchant = row['Description']
                amount = row['Amount']
                category = row['Category']
                description = row['Description']

                merchant = extract_merchant_name(merchant)

                writer.writerow({
                    'Date': date,
                    'Merchant': merchant,
                    'Amount': amount,
                    'Category': category,
                    'Description': description
                })

    else:
        print("File not found.")


read_csv()
