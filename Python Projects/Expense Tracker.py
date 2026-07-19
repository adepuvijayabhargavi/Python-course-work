#Expense Tracker project

expenses = [] #List of all expenses
print("Welcome to Expense Tracker: Use money wisely!")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3.View Total Expenses")
    print("4. Exit")

    choice = input(" Please Enter your choice : ")
    
#Add Expense
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        expenses.append({"amount": amount, "description": description})
        print("Expense added successfully!")

    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

    elif choice == '3':
        total_expenses = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: ${total_expenses:.2f}")

    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

     


