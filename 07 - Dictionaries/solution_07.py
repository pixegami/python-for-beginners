"""
Imagine you are making an online expense tracking app, 
and you are using a dictionary to store the total expenses for things you buy.

You want to add a new item to the dictionary - an "entertainment" expense of $20. 
You also spend an addition $12 on food and want to update the dictionary.
"""

total_expenses = {"food": 40, "transport": 0, "shopping": 190}

# Add an "entertainment" expense ($20)
total_expenses["entertainment"] = 20
# OR total_expenses.update({"entertainment": 20})
# OR total_expenses["entertainment"] = total_expenses.get("entertainment", 0) + 20
# What are the advantages of each way?

# Increase "food" expense (by $12)
total_expenses["food"] += 12
# OR total_expenses["food"] = total_expenses.get("food", 0) + 12

print(total_expenses)
