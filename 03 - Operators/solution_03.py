principal = 240_000
annual_rate = 0.05
years = 2

# Using the compound interest formula (https://g.co/kgs/Fa1yyX) with
# a compound period of 1 year:

new_value = principal * (1 + annual_rate) ** years
print(f"Compounded balance: {new_value}")
