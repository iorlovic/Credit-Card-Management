import csv
import os
import re


def extract_merchant_name(input_string):
    # Replace multiple spaces with a single space
    input_string = re.sub(r'\s+', ' ', input_string).strip()

    # Find matches for uppercase words followed by uppercase words with spaces, lowercase letters, or digits
    matches = re.findall(r'\b(?:[A-Z]+\s?)+[A-Z]+(?:[a-z\d]+)?(?=\s[A-Z]+\b)', input_string)

    if matches:
        merchant_name = matches[0]
    else:
        merchant_name = ""

    return merchant_name

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
