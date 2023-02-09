from datetime import datetime
from expense import Expense


def main():

    # Ask the user to add an expense.
    expense = get_expense()
    print(f"You've added {expense} to your expenses.")

    # Save the expense to a file.
    expenses = save_expense(expense)

    # Show the user the current expense breakdown.
    number_of_expenses = len(expenses)
    total_expenses = sum([expense.amount for expense in expenses])
    print(f"You have {number_of_expenses} expenses totalling ${total_expenses:.2f}.")

    # Show expenses by category.
    show_expense_by_category(expenses)

    # Show the user a rough estimate of how much they have left to spend per day.
    show_budget(total_expenses)


def save_expense(expense):
    current_date = datetime.now()
    expense_filename = f"expenses_{current_date.year}_{current_date.month}.csv"

    with open(expense_filename, "a") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")

    # Read the expenses from the file.
    expenses = []
    with open(expense_filename, "r") as file:
        for line in file:
            name, category, amount = line.strip().split(",")
            expenses.append(Expense(name, category, float(amount)))
    return expenses


def get_expense():
    print("Welcome to the expense tracker! 🤑")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount ($): "))
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category:")
        for index, category in enumerate(expense_categories):
            print(f"{index + 1}. {category}")

        category_index = int(input("Enter a category number: ")) - 1
        if category_index in range(len(expense_categories)):
            break
        else:
            print("Invalid category. Please try again.")

    expense_category = expense_categories[category_index]
    expense = Expense(expense_name, expense_category, expense_amount)
    return expense


def show_budget(total_expenses):
    print("\n💵 Budget")
    MONTHLY_BUDGET = 2000
    money_left = MONTHLY_BUDGET - total_expenses
    money_left_str = green(f"${money_left:.2f}")

    if money_left < 0:
        print(f"You're over budget by {money_left_str} this month.")
    else:
        print(f"You have {money_left_str} left to spend this month.")
        days_left = 30 - datetime.now().day
        money_per_day = money_left / days_left
        money_per_day_str = green(f"${money_per_day:.2f}")
        print(f"That's roughly {money_per_day_str} per day.")


def show_expense_by_category(expenses):
    print("\n📈 Expenses by category")
    categories = set([expense.category for expense in expenses])
    for category in categories:
        category_expenses = [
            expense for expense in expenses if expense.category == category
        ]
        category_total = sum([expense.amount for expense in category_expenses])
        print(f"{category}: ${category_total:.2f}")


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
