import json
from datetime import datetime
expenses = []

def add_expense():
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    
    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    print("Expense added successfully!")
    save_expenses()

def view_summary():
    total_spending = sum([expense['amount'] for expense in expenses])
    print(f"Total overall spending: ${total_spending}")
    
    category_spending = {}
    for expense in expenses:
        category = expense['category']
        if category not in category_spending:
            category_spending[category] = 0
        category_spending[category] += expense['amount']
    
    for category, total in category_spending.items():
        print(f"Total spending on {category}: ${total}")

def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved to file.")

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            global expenses
            expenses = json.load(file)
            print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No previous records found.")

def main_menu():
    load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Summary\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main_menu()