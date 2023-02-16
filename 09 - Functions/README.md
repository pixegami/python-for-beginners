# 09: Functions

In Python, a function is a block of code that can be reused multiple times. They can accept input (known as parameters or arguments). They can also "return" output too, which can be any type of data.

To use a function, you can "call" a function by its name. So remember the `print()` statement we've been using? That is a "function" we've been using. Now let's learn how to create our own.

### Example: A Simple Function

```python
def say_hello_to(name):
	greeting = f"Hello {name}!"
	return greeting

message = say_hello_to("jack")
print(message)
```

Let's break down the syntax. You can define a new function by using `def` keyword. And `say_hello_to` is the *name* of the function. You also have to have a pair of parentheses `()`, and then an argument (input) called `name`.

```python
def say_hello_to(name):
	# The rest of the code [...]
```

Moving on to the function body — this is the block of code that will run when the function is used or executed, and it's one indent level in from the function definition.

## Using (Calling) a Function

Just type the name of the function, along with the parentheses to tell Python that we want to run it.

If you don't have the parentheses, it won't run.

```python
def say_hello():
	print("Hello Jack!")

say_hello()  # "Hello Jack!"
say_hello()  # "Hello Jack!"
say_hello    # This won't run. You need the ().
```

## Passing Inputs (Arguments) to a Function

What if we want to the function to say "hello" to different people? We can make the function accept an input. This is called a "parameter", or an "argument".

The syntax for that is to just specify it in these brackets as part of the function definition. This will be the name of the argument, and you can call it whatever you want. I'm calling this one `name`.

Now in the scope of the function, I can use it just like a normal variable.

```python
def say_hello(name):
	print(f"Hello {name}!")
```

When I call this function now, I must pass an argument in as well, because the function is expecting it.

```python
say_hello("Jack")   # "Hello Jack!"
say_hello("Alice")  # "Hello Alice!"
say_hello("Bob")    # "Hello Bob!"
```

And each time this function runs, it'll receive one of these strings as the "name" argument, which is then accessible within the scope of the function.

## Returning Output

Beyond the *scope* (indent level) of the function, you won't be able to access anything you create within a function — including the arguments.

Anything new variable is created within the scope of the function will cease to exist beyond its scope. It's just there temporarily while the function executes.

```python
def say_hello(name):
	print(f"Hello {name}!")

print(name)  # Error!
```

So what happens if I **don't** want to *print* this greeting, but instead, store it in a variable as a string, so I can maybe send it in an email later?

```python
def say_hello(name):
	message = f"Hello {name}!"

print(message)  # Error!
```

It turns out functions also have a way to return output to you when you use it. You can do this with the `return` keyword like this.

```python
def say_hello(name):
	message = f"Hello {name}!"
	return message

jack_greeting = say_hello("jack")
print(say_hello("jack"))
```

When the function reaches the return statement, it will immediately exit. It will *short-circuit* the function so if you have any more code after the return statement, it will not be executed.

It will also "return" whatever value you put here. If you put nothing, it'll return `None`.

```python
def say_hello(name):
	message = f"Hello {name}!"
	return message

greeting = say_hello("jack")
print(greeting)  # None
```

So to summarise, you can use "return" to get an output from a function. This output can be stored in a variable, printed, or used in any way you want. 

This is helpful if you want your function to do some work, and use its output for something else (e.g. summing up a list of numbers).

## Positional Arguments

We can also add more than one parameter to the function. In fact we can add as many as we want. Just put a comma in the brackets and add another argument. These are called positional arguments.

```python
def say_hello(name, title):
	message = f"Hello {title} {name}!"
	print(message)
	return message
```

And again, to use it, just pass in the value you want when you call the function.

```python
say_hello("Jack", "Mr")
say_hello("Alice", "Ms")
say_hello("Bob", "Dr")
```

The positional ordering of data passed to function matters, because it corresponds to the position of the arguments.

## Keyword Arguments

It seems straightforward, but it cause bugs and confusion if you are working on a large project, and need to remember which positions things have to be in, especially if it's no obvious.

That's why we can also specify arguments by using keywords.

```python
say_hello((name="Jack", title="Mr")
say_hello((name="Alice", title="Ms")
say_hello((name="Bob", title="Dr")
```

The keywords simply correspond to the name of the function arguments that we defined in the function signature.

We also still have the option to use keyword arguments positionally.

```python
say_hello("Jack", "Mr")
```

## Default and Optional Arguments

Now, in a function like this, the `name` is an important piece of information to have. But the `title`? Maybe not so much. What if I wanted to make this argument optional?

That's easy as well. All I have to do is just specify a default value for it in the function definition.

```python
def say_hello(name, title=""):
	print(f"Hello {title} {name}!")
```

So here, if a title isn't provided to the function, then it's just going to default to an empty string. Now I can use only when I need to.

```python
say_hello(name="Jack")
say_hello(name="Alice")
say_hello(name="Bob", title="Dr")
```

> 👉 If you want to use optional parameters, they must come after all the required parameters. So I can't swap these around, and have an optional title first, then a name. I will get an error. All the required arguments must come first.

## Variadic Arguments

Sometimes we have to be able to accept an unknown number of arguments. To do this, we can use the `*` syntax. This will allow us to use the argument like a list.

```python
def say_hello(*names):
	for name in names:
		print(f"Hello {name}!")

say_hello("Jack")
say_hello("Jack", "Alice")
say_hello("Jack", "Alice", "Bob")
```

Here, we can now pass in as many names as we want, and the function will just loop over them and print out the greeting.

The `*` syntax is also useful for *unpacking* lists and dictionaries. We can unpack the contents of a list, and then pass them into the function.

```python
names = ["Jack", "Alice", "Bob"]
say_hello(*names)
# Same as typing say_hello("Jack", "Alice", "Bob")
```

> ⚠️ Be careful! Variadic arguments are the same as passing an actual list into a function!

```python
# These are NOT equivalent!
# This one receives 3 separate arguments.
say_hello("Jack", "Alice", "Bob")

# This one receives a single argument (which is a list).
say_hello(["Jack", "Alice", "Bob"])
```

## Common Mistakes With Functions

Can you see what's wrong with this piece of code?

```python
def shout(message):
	message += "!!!!"

hello = "Hello World"
shout(hello)
print(hello)
```

This function is supposed to add some exclamation mark to this message. Which it does, but when we print it here, it's doesn't have those exclamation marks added. Why not?

Well, here's a hint. It all has to do with the ***mutability*** of data-types.

Simply put, some data-types can change, and some cannot. All the primitive data-types (strings, integers, floats and booleans) are ***immutable***.

So when we're adding the exclamation marks to this message variable here, it's only affected the message variable in the scope of this function. 

```python
message += "!!!!"
```

It doesn't affect the value of the original message itself. This is basically a new ***copy*** of the original message. That's why when we print the original "hello" message, it hasn't changed.

To fix this up, we'll need to return the updated message.

```python
def shout(message):
	message += "!!!!"
	return message

hello = "Hello World"
hello = shout(hello)
print(hello)  # Hello World!!!!
```

We can store this in a new variable, or we can re-use the same variable name by overwriting it.

## Using Mutable Datatypes with Functions

Inversely, if you pass in a **mutable** data type into a function, like a list, you can actually change its contents within the function. 

You don't have to return it, because the argument acts as a *reference* to the real instance of that data.

```python
def double_list_values(my_list):
	for i in range(len(my_list)):
		my_list[i] *= 2
```

Consider this example where we have a function to double all of the values in a list. Here we don't need to return the doubled list, we can update its values directly within the scope of the function.

```python
original_list = [1, 2, 3]
print(original_list) # [1, 2, 3]

double_list_values(original_list)
print(original_list) # [2, 4, 6]
```

And when we use a function to modify something outside the scope of the function, this is called a "side-effect".

## Abstraction

The major advantage of functions is that they let us build useful *abstractions* on code that is otherwise not very intuitive to read.

And if you hear the word "abstraction" in software engineering, it means to "hide away the complexity" of something from a user (and sometimes that user is yourself), and just expose the its key elements.

Basically, it means to simplify something in a really useful way. To me, this is the core value of a function.

### Example of Abstraction

Take a look at this formula. This represents something that is very common in day to day life. You may have seen it before! Can you tell what it is, or what it does?

```
x * (1 + y) ** z
```

What about if we turn these variable names into something meaningful? 

```python
principal * (1 + rate) ** years
```

Does this help clarify what the formula does? It's calculating the interest for a given principle amount, interest rate, and time period (like our exercise in Chapter 3). It's commonly used for a bank deposit or a home loan.

```python
principal = 1000
rate = 0.05
years = 2
interest = principal * (1 + rate) ** years
```

Now let's turn it into a function.

```python
def calc_interest(principal, rate, years):
	return principal * (1 + rate) ** years
```

So that now we want to use it, it's just really straightforward. 

```python
new_value = calc_interest(principal=1000, rate=0.05, years=2)
```

We went from something that was cryptic to something that most humans will understand just by reading it, even if they don't know how to code.

And I think one of the most important skills for a programmer to have is exactly being able to do this. It's not advanced mathematics or memorising a bunch of algorithms.

But being able to turn complex ideas into simple abstractions, so that we can build more complex things from simple parts.

```python
 # Before
x * (1 + y) ** z

 # After
new_value = calc_interest(principal=1000, rate=0.05, years=2)
```

# Coding Exercise 09: Functions

Write a function `apply_discount()` that takes two arguments: the original price and the discount percentage, and returns the discounted price. 

Additionally, If the discount is more than 100%, the new price should be fixed at 0 (and not negative).

```python
# TODO: Implement the "apply_discount" function.

# Test it like this...
new_price = apply_discount(1000, percent=10)
print(new_price) # Should be 900
```

Once you've given it a go, check out the [solution here](./solution_09.py).
