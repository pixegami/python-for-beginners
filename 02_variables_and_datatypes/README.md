# 02: Variables and Data Types

Variables in Python are how we can store data and how we can refer to it later on, or whenever we need it to do something with.

Here are some examples.

```python
x = 9
```

```python
y = "hello"
```

Let's get hands on and write this into a program. Create a new file. I'm gonna call this `main.py`, but you can call it anything you want.

A variable has a name and a value. The name can be almost anything. It should be descriptive, and explain what the purpose of the value is.

What happens if we try to use a variable that isn't defined?

```python
print(z)
```

We get an error. That's because we always have to declare a variable before we can use it.

```text
NameError: name 'z' is not defined
```

Here are some example of good Python variables names.

### ✅ Good Variable Names

```python
x
account_id
student_name
tax_rate
temperature_fahrenheit
is_valid
```

A variable is associated with a value, which can be things like a number, a word, or more complex things that we'll learn about later on.

### 👉 Example Values

```python
x = 6
account_id = "08293310"
student_name = "jack"
tax_rate = 0.21
temp_fahrenheit = 70
is_valid = True
```

### 🔥 Bad Variable Names

```python
min          # Reserved word
1_var        # Cannot start with number!
var_1        # Not descriptive
StudentName  # Incorrect casing
proc_ctr     # Too abbreviated
distance     # Should have unit (km, m, etc)
```

---

### Two Hard Things

Don't worry if you struggle to come up with good variable names. It's a skill that takes time to develop.

```text
There are only two hard things in Computer Science:
cache invalidation and naming things.

— Phil Karlton
```

---

## Example Usage of Variables

And here's some examples of how we can use variables in our programs (and what problems they solve in different scenarios).

### 🕹️ Games

```python
hp = 120
power = 10
move_speed = 3.4
```

### 🍔 Food Ordering App

```python
item_name = "burger"
price_usd = 8.99
is_vegetarian = False
```

### 📈 Finance App

```python
symbol = "AAPL"
quantity = 8
order_type = "BUY"
```

## Data Types

Now let's take a closer look at these 'values.' They are data, or basically - ways of representing information about the world.

There are four primitive data types in Python. And these are the building blocks to more complex data structures that we'll see later.

### Primitive Data Types

```python
int      # Integer (whole numbers)
float    # Float (numbers with decimals)
str      # String (literals, words, text)
bool     # Boolean (either True or False)
```

And a couple of extra things to be aware of with data types: Strings are case-sensitive. And boolean values (True and False) need to be capitalized.

### 👉 Examples

```python
x = 8                # int
y = 2.32             # float
name = "Jack"        # str
likes_coffee = True  # bool
```

The reason for having these four distinct types has something to do with efficiency, and with how they are represented in computer memory.

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

## Example Usage of Datatype

### 🧩 What Datatypes Would You Use?

- ✏️ Item Name
- ✏️ Quantity
- ✏️ Price
- ✏️ In Stock?

Pause the video and have a think about it.

```python
item_name = "apple"
quantity = 4
price = 4.99
in_stock = True
```

## Printing in Python

There's also several ways to "print" information in Python. Printing is how we make some information appear on the screen

```python
x = 12
print(x)  # 12
```

```python
x = 12
y = 24
print(x, y)  # 12, 24
```

```python
x = 12
print("Hello", x)  # Hello, 12
```

```python
x = 12
print(f"The value of x is {x}")
# The value of x is 12
```
