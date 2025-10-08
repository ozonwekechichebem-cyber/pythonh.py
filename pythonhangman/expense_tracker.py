# Personal expense tracker
import json

FILENAME = "expenses.txt"


def load_expenses():
    """Load expenses from file."""
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    """Save expenses to file."""
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Add a new expense entry."""
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {"date": date, "description": description, "amount": amount}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid amount! Please enter a number.\n")


def view_expenses(expenses):
    """Display all saved expenses."""
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        for exp in expenses:
            print(f"{exp['date']} - {exp['description']} - ₦{exp['amount']}")
        print() # Blank line after list


def view_total(expenses):
    """Calculate and display total amount spent."""
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Amount Spent: ₦{total}\n")


def main():
    """Main program loop."""
    expenses = load_expenses()

    while True:
        print("===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Amount Spent")
        print("4. Exit")
        print("====================================")

        choice = input("Select an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.\n")
if __name__ == "__main__":
    main()

#==== PERSONAL EXPENSES TRACKER ====
# 1. Add _expense
# 2. View view_expenses
# 3. view_Total Amount Spent
# 4. exit
# =======================================
# Select option:1
# Enter date (YYYY-MM-DD)
# 2025-10-08
# Enter description: Lunch
# Enter amount: 1200
# Expense added successfully!

# Select an option:2
# 2025-10-06 - Lunch - #1200

# select an option:3
# Total amount spent: #1200

# Select an option:4
# Exiting program... Goodbye!

