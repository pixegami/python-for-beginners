"""
Write a short Python script to store the information in variables, and then print it out in a nice format (for an e-commerce website, for example):

- Item Name (e.g. "apple")
- Quantity (e.g. 4)
- Price (e.g. $0.50)
- In Stock? (e.g. Yes/No)

"""

# The variable names should be short, descriptive, and in snake_case.
item_name = "apple"
quantity = 4
price_usd = 0.50
in_stock = True

# Print out the information in a nice format using f-strings.
print(f"Item Name : {item_name}")
print(f"Quantity : {quantity}")
print(f"Price : ${price_usd}")
print(f"In Stock? : {in_stock}")
