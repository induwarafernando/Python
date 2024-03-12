import json

# Initialize the master list to store transactions
transactions = []

# Function to add a new transaction
def add_transaction():
    transaction_id = len(transactions) + 1
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    transactions.append([transaction_id, date, description, amount, category])
    print("Transaction added successfully.")

# Function to view all transactions
def view_transactions():
    print("\nTransactions:")
    for transaction in transactions:
        print(f"ID: {transaction[0]}, Date: {transaction[1]}, Description: {transaction[2]}, Amount: {transaction[3]}, Category: {transaction[4]}")

# Function to update a transaction
def update_transaction():
    transaction_id = int(input("Enter the transaction ID to update: "))
    for transaction in transactions:
        if transaction[0] == transaction_id:
            transaction[1] = input("Enter the new date (YYYY-MM-DD): ")
            transaction[2] = input("Enter the new description: ")
            transaction[3] = float(input("Enter the new amount: "))
            transaction[4] = input("Enter the new category: ")
            print("Transaction updated successfully.")
            return
    print("Transaction not found.")

# Function to delete a transaction
def delete_transaction():
    transaction_id = int(input("Enter the transaction ID to delete: "))
    for i, transaction in enumerate(transactions):
        if transaction[0] == transaction_id:
            del transactions[i]
            print("Transaction deleted successfully.")
            return
    print("Transaction not found.")

# Function to calculate summary statistics
def summary():
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction[3] > 0:
            total_income += transaction[3]
        else:
            total_expenses += transaction[3]
    print(f"\nSummary:")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Net Balance: {total_income + total_expenses}")

# Function to save data to a JSON file
def save_data():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)
    print("Data saved successfully.")

# Function to load data from a JSON file
def load_data():
    global transactions
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

# Main program loop
def main():
    load_data()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Summary")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_transaction()
        elif choice == 2:
            view_transactions()
        elif choice == 3:
            update_transaction()
        elif choice == 4:
            delete_transaction()
        elif choice == 5:
            summary()
        elif choice == 6:
            save_data()
        elif choice == 7:
            load_data()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
