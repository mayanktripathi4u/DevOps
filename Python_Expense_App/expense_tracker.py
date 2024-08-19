# from DevOps.Python_Expense_App.expense import Expense
from expense import Expense
from typing import List
import calendar
import datetime

def main():
    print(f"🎯 Running Expense Tracker!")

    # Get user input for expense.
    # expense = get_user_expanse()
    # print(expense)
    expense_file_path = 'expenses.csv'
    budget = 2000

    # Write expenses to a file
    # save_expense_to_file(expense, expense_file_path)

    # Read file and Summarize Expenses.
    summarize_expenses(expense_file_path, budget)

    pass

def get_user_expanse():
    print(f"Getting User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = input("Enter Expense Amount: ")
    # expense_name = input("Enter Expense Name: ")

    expense_categories = [
        "🍲 Food", 
        "🏠 Home", 
        "🏢 Work",
        "🎉 Fun",
        "🪄 Misc",
    ]

    while True:
        print("Select a Category: ")
        for i, cateory in enumerate(expense_categories):
            print(f"{i}. {cateory}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a Category Number {value_range} : ")) - 1

        if selected_index in range(len(expense_categories)):
            category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, amount=expense_amount, category=category)
            return new_expense
        else:
            print("Invalid Category. Please try again")
        # break

    print(f"You've entered {expense_name} for ${expense_amount}. Selected Category {selected_index}")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense : {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")
    

def summarize_expenses(expense_file_path, budget = 100):
    print(f"Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            stripped_line = line.strip()
            name, category, amount = stripped_line.split(",")
            # print(name, category, amount)
            line_expense = Expense(name=name, category=category, amount=float(amount))
            # print(line_expense)
            expenses.append(line_expense)
    # print(expenses)
    amount_by_category  = {}
    for exp in expenses:
        key = exp.category
        if key in amount_by_category:
            amount_by_category[key] += exp.amount
        else:
            amount_by_category[key] = exp.amount
    # print(amount_by_category)

    print("Expenses by Category : ")
    for key, amount in amount_by_category.items():
        print(f"   {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You have spent ${total_spent:.2f} this Month! ")
    remaining_budget = budget - total_spent
    print(f"Budget Remaining : ${remaining_budget:.2f}")

    # Get current date
    now = datetime.datetime.now()

    # Get the Number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    print(f"Remaining days in the current month: {remaining_days}")
    daily_budget = remaining_budget / remaining_days
    print(f"Budget per Day : ${daily_budget:.2f}")
    print(green(f"Budget per Day : ${daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()
