import csv
import os
print("================================")
print("    STUDENT EXPENSE TRACKER")
print("================================")

name = input("\nEnter your name: ")

# Store expenses in a list
expenses = []


if os.path.exists("expenses.csv"):
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append((row[0], float(row[1])))

while True:
    print("\n--- MENU ---")
    print("1. Add Expense")
    print("2. View All Expenses and Total")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")
        
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                expenses.append((expense_name, amount))
                
                with open("expenses.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([expense_name, amount])

        except ValueError:
            print("Invalid amount! Please enter a valid number.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print(f"\nExpenses for {name}:")

            for number, expense in enumerate(expenses, start=1):
                print(f"{number}. {expense[0]} - Rs. {expense[1]:.2f}")

            total = sum(expense[1] for expense in expenses)
            print(f"\nTotal Spending: Rs. {total:.2f}")

    elif choice == "3":
        print(f"Thank you, {name}! Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")
