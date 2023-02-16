# 01: How to Install and Run Python

Python is available for all OS platforms (Windows, Mac and Linux).

## Windows 
1. Download the latest version of Python from the [Python downloads page](https://www.python.org/downloads/) 
2. Run the installer and follow the instructions. Make sure to check the box to add Python to your `PATH`.

## Mac and Linux

If you use Mac or Linux, your computer should already come with Python, so you should be able to skip this step.

Otherwise, you can follow the same instructions as above, just make sure to download the correct version for your system.

## Checking Python Version

To check the version of Python installed on your system, open a terminal and type: 

```bash
python --version
```

You should see it print out your Python version. For example:

```
Python 3.10.8
```

If you end up having **Python version 2** instead of version 3, then try this command instead.

```bash
python3 --version
```

We will need Python 3.6 or above. If it doesn't work, then go back to the installation step and make sure you have at least version 3.6.

## Python Interpreter

Before we write some code, let's run the Python interpreter. Type in this command and press Enter.

```bash
python
```

Now in the terminal, you can use the Python interpreter. Here's some basic things to try (type and press `Enter` after each line):

```python 
print("Hello World!")
x = 5
y = 10
z = x + y
print(z) 
```

When you're done, type `exit()` and press Enter to exit the Python interpreter. You can also press Ctrl+D to exit.

## How does Python work?

What you've just run is called the "Python interpreter". The Python interpreter is a program that reads and executes the Python code that you write.

Python is an interpreted language, which means that the code you write isn't actually translated into a language that the computer understands and runs directly. Instead, it's read and executed by the Python interpreter, line by line.

When you write a Python program, you write it in a text file, and save it with the extension `.py`. This file is called a Python script.

What we'll be learning today is writing these Python scripts that the Python interpreter (the thing you just installed), will run for us.

## Code Editor

Now let's write our first Python script. For this you can use any text editor. But I recommend [VSCode](https://code.visualstudio.com). 

It's simple and it's free, but it's also powerful enough to use professionally. For the rest of this tutorial, I'll assume you have VSCode.

But if VSCode isn't for you, here are three other suitable IDEs or code editors for Python:

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](https://www.sublimetext.com)

And if you don't have access to install a code editor, you can also use an online editor (called REPL) such as:

- [Repl.it](https://repl.it/languages/python3)
- [PythonAnywhere](https://www.pythonanywhere.com)

## Write Your First Python Script

Create a folder somewhere on your computer for this tutorial. And then open up that folder in VSCode (or your editor of choice).

Once you have that folder, create a new file, and name it `hello.py`.

And in that file write this line:

```python
print("Hello World! 👋")
```

## Run Your Python Script

If you're using VSCode, it's really easy. You should just be able to press `F5` (or `Ctrl+F5` on Windows) to run your script.

If you're using a different editor, you'll need to open up a terminal, and then run your script with the `python` command.

```bash
python hello.py
```

Once you've done that, you should see the output `Hello World!` 👋  in your terminal.

---

🎉 Congratulations, you've written and run your first Python script! Keep going! 👉