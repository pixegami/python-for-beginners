# 10: User Input

Ultimately, we write Python code to do useful things for people. So we need a way to get input data from the outside world somehow—whether that's a direct input they type into the console, a local file (like an Excel or PDF file), or over the internet.

### Ways to Get User Input
- 👉  Direct User Input
- 👉  Local Files
- 👉  Over the Internet

## Direct User Input

In our upcoming final project, we want to build a **personal expense tracking app**. We'll need users to enter the name and the amount of the expense.

The easiest way to do that is using this in-built Python function:

```
input()
```

If you run this in the terminal, the Python script will stop at this statement and wait for the user to type something with their keyboard and press `Enter`.

We can make it show a text prompt. by putting a string in there.

```
input("Enter your name: ")
```

To store the value that the user types in, we can use the assignment operator to set that value into a variable.

```python
user_name = input("Enter your name: ")
print(f"Your name is {user_name}"")
```

That's because this input statement is a built-in function in Python, and when the user types something into the terminal, the function will return (or evaluate to) the thing that the user typed.

### ⚠️ `input()` always returns a string!

The result from using input is always going to be a string. Even if you enter a number. And if you try to use it directly as a number, like try to use arithmetic operators on it, it will either fail or give you strange results.

```python
x = input("Enter a number: ")
print(f"x is a {type(x)}")
```

But you can convert a string of digits into a number like this. And this is called "casting" - when you convert one type of data into another.

```python
x = int("32")
print(x * 100)
```

# Other Ways To Get User Input

Although it is out of our scope for this tutorial series, let's take a quick look at various other ways we can get user input from Python.

## CLI Arguments

It's possible to pass in arguments to the Python program when you run it from the command line. This is called "command line arguments". 

The arguments are stored in the `sys.argv` list and can be used in the program.

```python
python main.py --verbose
```

```python
import sys

if "--verbose" in sys.argv:
    print("Verbose mode is enabled!")
```

But if you were serious about adding arguments like this, I suggest using the built-in the [argparse](https://docs.python.org/3/library/argparse.html) library to do the heavy lifting.

## File IO

It is possible to read input from a file as well, whether that's a PDF file, image file, CSV spreadsheet, or just a plain text file.

```python
with open("input.txt", "r") as f:
    input_data = f.read()
```

We have to use this `with` keyword because when you "open" a file, it will stay open until you explicitly close it. And if you forget to close it, it can cause all kinds of problems later on.

Using the `with` keyword creates something called a "context manager" for this, and it will automatically close the file for us when we are done using it (and our code exits its scope).

To write to a file we can use the `open` function again with the `w` mode.

```python
with open("output.txt", "w") as f:
    f.write("Hello World From Python!")
```

## REST APIs

Probably (by far) the most useful way to communicate with the world from Python is by having it talk to other apps over the internet.

There's a lot of ways for this communication to happen, but the most common way is with REST APIs. This is by sending a structured message to an `http` endpoint and getting response back.

Here's an example using GitHub's user API to get info about my user account. You can change it to your username if you have a GitHub profile.

```python
import requests

ENDPOINT = "https://api.github.com/users/pixegami"
response = requests.get(ENDPOINT)
data = response.json()

print(data["name"])  # Jack
print(data["location"])  # Sydney, Australia
```

---

# Coding Exercise 10: Input

Write a program that prompts the user for their name and age, and save that information into a file called `user_info.txt`.

```python
[insert]
```

Once you've given it a go, check out the [solution here](./solution_10.py).