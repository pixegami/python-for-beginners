"""
Write a program that prompts the user 
for their name and age, and save that information 
into a file called `user_info.txt`.
"""

# Prompt user for input
name = input("What is your name? ")
age = input("What is your age? ")

# Write to file
with open("user_info.txt", "w") as f:
    f.write(f"{name} {age}\n")
