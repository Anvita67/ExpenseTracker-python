def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    with open("expenses.txt", "a") as file:
        file.write(f"{description} - {amount}\n")
    print("Expense added!")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            if expenses:
                print("\nYour Expenses:")
                total = 0
                for expense in expenses:
                    print(expense.strip())
                    total += float(expense.strip().split(" - ")[1])
                print(f"Total Spent: {total}")
            else:
                print("No expenses recorded yet!")
    except FileNotFoundError:
        print("No expenses recorded yet!")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
