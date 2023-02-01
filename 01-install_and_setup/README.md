# How to Install and Run Python

You can use Python on Mac, Windows, or Linux.

## Windows

If you're a Windows user then you can go to the [official Python website](https://python.org) and follow the instructions there.

For Windows you'll also want to click "Yes" when asked to add it to PATH.

## Mac and Linux

If you use Mac or Linux, your computer should already come with Python, so you should be able to skip this step.

## Checking Python Version

Next, let's check our Python installation (or the existing Python that comes with our machine, if you're on Mac or Linux) by opening up the terminal.

If you've never used a terminal before, then it's just an way to interact with our computer via text.

Now don't worry if your terminal looks different to mine. They should still behave the same way.

Type in this command and press Enter.

```bash
python --version
# Python 3.10.8
```

If you end up having Python version 2 instead of version 3, then try this command instead.

```bash
python3 --version
# Python 3.10.8
```

We will need Python 3.6 or above. If it doesn't work, then go back to the installation step and make sure you have at least version 3.6.

Otherwise check in the video description and comments for help.

## Python Interpreter

Before we write some code, let's run the Python interpreter.

Type in this command and press Enter.

```bash
python
```

Now in the terminal, you can use Python as a calculator.

```python
2 + 3
```

## How does Python work?

What you've just run is called the "Python interpreter". Outside of the tech world, the word "interpreter" usually refers to someone who translates from one language to another.

You can think of the Python interpreter as a translator too. It translates human readable language (what we call a Python script), into machine instructions–whether that's adding numbers, uploading a video, or actuating a robotic arm.

But another way to think about it is that the Python interpreter is like a game console. Like a Super Nintendo. It's got system and the capability to run things.

And the Python scripts, are like the game cartridges. You plug in a cartridge, and the console will 'play' whatever is written on that cartridge.

What we'll be learning today is writing these Python scripts that the Python interpreter (the thing you just installed), will run for us.

## Code Editor

Now let's write our first Python script. For this you can use any text editor. But I recommend VSCode. It's simple and it's free, but it's also powerful enough to use professionally.

```
https://code.visualstudio.com
```

## Write Your First Python Script

Create a folder somewhere on your computer for this tutorial. And then open up that folder in VSCode.

Once you have that folder, create a new file, and name it:

```
hello.py
```

And in that file write this line:

```python
print("Hello World!")
```

Now let's run it! How do we run it?

## Run Your Python Script

If you're using VSCode, it's really easy. You should just be able to press this little play button up here, and the script should run in this little tab, which is actually an in-built terminal.

Up here you can see the commands that VSCode uses to run your script.

If you want to run them yourself from the regular terminal that we used before, you can copy these commands there and run them there too.

Or if your terminal is already navigated to this folder, then we can run it with just the name of the script, because the script is local to us now and is therefore visible to our terminal.

```bash
python hello.py
```

And eventually, you may have a lot of different versions of Python interpreters on your system. This is common if you want to set up separate Python environments for different projects.

To select the interpreter version that VSCode uses, click in this little version number tab at the bottom right of the screen, and you'll get a pop-up to select between the different Python interpreters you have installed on your machine.
