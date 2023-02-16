"""
Task: Given a list of shopping expenses, print the top 3 expenses.
"""

shopping_expenses = [24, 60, 8, 92, 160, 80, 250, 20, 10]

# (Optional) Create a copy of the original list (so we don't modify the original).
shopping_expenses_copy = shopping_expenses[:]

# Sort the list in-place.
shopping_expenses_copy.sort()

# The list will be in ascending order, so reverse it.
shopping_expenses_copy.reverse()

# Slice the first 3 elements.
top_3_expenses = shopping_expenses_copy[:3]
print(f"Top 3 expenses: {top_3_expenses}")
