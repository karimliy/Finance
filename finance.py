import handler

def add_transaction(transactions):
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    type_ = input("Type (income/expense): ").lower()

    transaction = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
        "type": type_
    }
    transactions.append(transaction)
    handler.save_transactions(transactions)
    print("Transaction added successfully!\n")

def view_transactions(transactions):
    for t in transactions:
        print(t)

def generate_summary_report(transactions):
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expense

    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}\n")

def main():
    transactions = handler.load_transactions()
    
    
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Summary Report")
    print("4. Exit")
    
    while True:
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            handler.generate_summary_report(transactions)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
