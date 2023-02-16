"""
Print the following pattern using for loop:

0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
"""

for i in range(5):
    message = ""
    for sub_number in range(i + 1):
        message += f"{sub_number} "
    print(message)
