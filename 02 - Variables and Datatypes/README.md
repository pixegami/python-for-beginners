# 02: Variables and Data Types

Variables in Python are how we can store data and how we can refer to it later on, or whenever we need it to do something with.

Here's some examples of how to define a variable, then print it out to our console:

```python
x = 9
print(x)  # 9
```

```python
y = "hello"
print(y)  # "hello"
```

Variables must be defined before you can use them. If you haven't defined it first, and try to use it, you will get an error:

```python
print(z)
# NameError: name 'z' is not defined
```

## Naming Variables

You can name your variables in Python _almost_ anything you want.

For instance, both `user_name` and `userName` are valid Python variable names, but one is "better" than the other because it uses "snake case" (lower case with underscores), which aligns with Python naming conventions.

Here are the rules and guidance for naming variables in Python:

- Can contain letters, numbers, and underscores
- Cannot start with a number
- Should not contain spaces or special characters
- Cannot be one of Python's [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
- Generally follows [PEP8 naming conventions](https://peps.python.org/pep-0008/#descriptive-naming-styles)
- Should be descriptive and easy to remember

### ✅ Good Variable Names

Good variable names should be short but descriptive.

```python
x
account_id
student_name
tax_rate
temperature_fahrenheit
is_valid
```

### 👉 Example Values

A variable is associated with a value, which can be things like a **number**, a **word**, or more complex things that we'll learn about later on.

Here's how we'd create variables and assign them a value:

```python
x = 6
account_id = "08293310"
student_name = "jack"
tax_rate = 0.21
temp_fahrenheit = 70
is_valid = True
```

If we want to create variable but don't know what it's value is going to be, we can also assign it `None`, which is a special reserved word in Python:

```python
account_id = None
```

### 🔥 Bad Variable Names

Here are some examples of variable names that are either bad, or outright invalid.

```python
min          # Reserved word
1_var        # Cannot start with number!
var_1        # Not descriptive
StudentName  # Incorrect casing
proc_ctr     # Too abbreviated
distance     # Should have unit (km, m, etc)
```

### Naming is hard!

Don't worry if you struggle to come up with good variable names. It's a skill that takes time to develop.

> There are only two hard things in Computer Science: cache invalidation and naming things. — Phil Karlton

---

## Example Usage of Variables

And here's some examples of how we can use variables in our programs (and what problems they solve in different scenarios).

### 🕹️ Games

In a game, you might want to store information about a character, like their hitpoints, power, and move speed.

```python
hp = 120
power = 10
move_speed = 3.4
```

### 🍔 Food Ordering App

In an online food ordering app, you might want to store information about a specific item, like its name, price, and whether it's vegetarian or not.

```python
item_name = "burger"
price_usd = 8.99
is_vegetarian = False
```

### 📈 Finance App

In a finance app, you might want to store information about a stock order, like its symbol, quantity, and order type.

```python
symbol = "AAPL"
quantity = 8
order_type = "BUY"
```

## Primitive Data Types

Now let's take a closer look at these 'values.' They are data, or basically - ways of representing information about the world.

There are four primitive data types in Python. And these are the building blocks to more complex data structures that we'll see later.

```python
int      # Integer (whole numbers)
float    # Float (numbers with decimals)
str      # String (literals, words, text)
bool     # Boolean (either True or False)
```

And a couple of extra things to be aware of with data types: Strings are case-sensitive. And boolean values (`True` and `False`) need to be capitalised. Here's some examples:

```python
x = 8                # int
y = 2.32             # float
name = "Jack"        # str
likes_coffee = True  # bool
```

The reason for having these four distinct types of data is to ensure that the data is stored in the most efficient, and accurate, way possible.

Each data type requires a different amount of memory for storage, and having the wrong data type could potentially lead to inaccuracies.

But more importantly, the data type also gives us a clue about what we can DO with the data. For example, I can add two integers together.

```python
 # Adding integers
print(2 + 2)  # 4
```

I can also add an integer with a float.

```python
 # Add int with float
print(2 + 3.5)  # 5.5
```

I can also add two strings, but that would behave differently.

```python
 # Adding two strings
print("2" + "2") # "22"
```

Strings are characters, and have no numerical value. So when I add them, it treats them as if we've just cut letters out of the newspaper and pasted them together like you see in movie ransom notes.

## Printing in Python

There's also several ways to "print" information in Python. Printing is how we make some information appear on the screen

We can use the `print()` function to print information:

```python
print("Hello World!")  # Hello World!
```

The `print()` function can also be used to "print" the value of variables:

```python
x = 12
print(x)  # 12
```

We can also print multiple values at once:

```python
x = 12
y = 24
print(x, y)  # 12, 24
```

We can also combine text and variables in our print statements:

```python
x = 12
print("Hello", x)  # Hello, 12
```

We can also use a formatting string (f-string) to print out variables. This is a popular approach because it allows us to easily combine text and variables:

```python
x = 12
print(f"The value of x is {x}")
# The value of x is 12
```

---

# Coding Exercise 02: Variables

Write a program that prints out the details of an item in a shop.
You need to model the following information:

- ✏️ Item Name (e.g. "apple")
- ✏️ Quantity (e.g. 4)
- ✏️ Price (e.g. $0.50)
- ✏️ In Stock? (e.g. Yes/No)

Write a short Python script to store the information in variables, and then print it out in a nice format.

When you've had a go, see the [solution here!](./solution_02.py).
