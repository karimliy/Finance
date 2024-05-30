import json

FILE_PATH = 'transactions.json'

def load_transactions():
    try:
        with open(FILE_PATH, 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []
    return transactions

def save_transactions(transactions):
    with open(FILE_PATH, 'w') as file:
        json.dump(transactions, file, indent=2)