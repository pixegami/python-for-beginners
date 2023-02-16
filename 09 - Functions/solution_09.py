"""
Write a function `apply_discount()` that takes two arguments:
the original price and the discount percentage, and returns the discounted price.
"""


def apply_discount(price, percent):
    if percent >= 100:
        # If discount is 100% or more, the price is free.
        return 0
    else:
        # Otherwise, calculate the discounted price.
        discount = price * percent / 100
        return price - discount


new_price = apply_discount(1000, percent=10)
print(new_price)  # Should be 900

new_price = apply_discount(900, percent=5)
print(new_price)  # Should be 855

new_price = apply_discount(10, percent=200)
print(new_price)  # Should be 0
