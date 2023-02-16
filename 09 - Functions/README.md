# Functions

## Functions

In Python, a function is a block of code that can be reused multiple times. 

They can accept input (known as parameters or arguments). They can also "return" output too, which can be any type of data.

### Functions
- Re-usable code
- Can accept input
- Can return output

So here's an example of very simple function.

```python
def say_hello_to(name):
	greeting = f"Hello {name}!"
	return greeting

message = say_hello_to("jack")
print(message)
```

So let's break down the syntax. You can define a new function by using this "def" keyword. And then this part is the name of the function.

You also have to have a pair of parentheses, and then a colon.

Now we move on to the function body. This is the block of code that will run when the function is used or executed, and it's one indent level in from the function definition.

And this is how you can use a function. Just type the name of the function here, along with the parentheses to tell Python that we want to run it.

If you don't have the parentheses, it won't run.

```python
def say_hello():
	print("Hello Jack!")

say_hello()
say_hello()
say_hello()
```

And you can use it as many times as you want.

Now what if we want to the function to say "hello" to different people? We can make the function accept an input. This is called a "parameter", or an "argument".

And the syntax for that is to just specify it in these brackets as part of the function definition.

This will be the name of the argument, and you can call it whatever you want. I'm calling this one "name".

Now in the scope of the function, I can use it just like a normal variable.

```python
def say_hello(name):
	print(f"Hello {name}!")
```

When I call this function now, I must pass an argument in as well, because the function is expecting it.

```python
say_hello("Jack")
say_hello("Alice")
say_hello("Bob")
```

And each time this function runs, it'll receive one of these strings as the "name" argument, which is then accessible within the scope of the function.

## Returning Output

Beyond the scope of the function though, you won't be able to access it anymore.

```python
def say_hello(name):
	print(f"Hello {name}!")

print(name)  # Error
```

In fact, anything new variable is created within the scope of the function will cease to exist beyond its scope. It's just there temporarily while the function executes.

So what happens if I don't want to print this greeting, but instead, store it in a variable as a string, so I can maybe send it in an email later?

```python
def say_hello(name):
	message = f"Hello {name}!"

print(message)  # Error
```

Well, it turns out functions also have a way to return output to you when you use it.

You can do this with the `return` keyword like this.

```python
def say_hello(name):
	message = f"Hello {name}!"
	return message

jack_greeting = say_hello("jack")
print(say_hello("jack"))
```

When the function reaches the return statement, it will immediately exit. It will short-circuit the function so if you have any more code after the return statement, it will not be executed.

It will also "return" whatever value you put here. If you put nothing, it'll return `None`. You can try it out.

And by "return" I mean that whenever this function is executed, it will evaluate into this piece of data. 

So I can use that data however I want. I can store it in a new variable, or I can just print it directly.

## Multiple Arguments

We can also add more than one parameter to the function. In fact we can add as many as we want. Just put a comma in the brackets and add another argument.

Let's add a "title" to the name.

```python
def say_hello(name, title):
	message = f"Hello {title} {name}!"
	return message
```

And again, to use it, just pass in the value you want when you call the function.

```python
print(say_hello("Jack", "Mr"))
print(say_hello("Alice", "Ms"))
print(say_hello("Bob", "Dr"))
```

The positional ordering of data passed to function matters, because it corresponds to the position of the arguments.

It seems straightforward, but it cause bugs and confusion if you are working on a large project, and need to remember which positions things have to be in, especially if it's no obvious.

That's why we can also specify arguments by using keywords.

And it looks like this.

```python
print(say_hello((name="Jack", title="Mr"))
print(say_hello((name="Alice", title="Ms"))
print(say_hello((name="Bob", title="Dr"))
```

And the keywords simply correspond to the name of the function arguments that we defined here.

Don't you think that's much easier to read as well?

Now, in a function like this, the name is an important piece of information to have. But the title? Maybe not so much. What if I wanted to make this argument optional?

In Python that's easy as well. All I have to do is just specify a default value for it in the function definition.

Now if you want to use optional parameters, they must come after all the required parameters. 

So I can't swap these around, and have an optional title first, then a name. I will get an error. All the required arguments must come first.

```python
def say_hello(name, title=""):
	print(f"Hello {title} {name}!")
```

So here, if a title isn't provided to the function, then it's just going to default to an empty string.

And now I can use only when I need to.

```python
say_hello(name="Jack")
say_hello(name="Alice")
say_hello(name="Bob", title="Dr")
```

## Common Mistakes With Functions

Now there is a common mistake I see many students make when working with functions. I've made it myself many times.

For example, can you see what's wrong with this piece of code?

```python
def shout(message):
	message += "!!!!"

hello = "Hello World"
shout(hello)
print(hello)
```

This function is supposed to add some exclamation mark to this message. Which it does, but when we print it here, it's doesn't have those exclamation marks added.

Why not?

Well, here's a hint. It all has to do with the mutability of data-types.

Simply put, some data-types can change, and some cannot. All the primitive data-types (strings, integers, floats and booleans) are immutable.

So when we're adding the exclamation marks to this message variable here, it's only affected the message variable in the scope of this function. 

It doesn't affect the value of the original message itself. This is basically a new copy of the original message. That's why when we print the original "hello" message, it hasn't changed.

To fix this up, we'll need to return the updated message.

```python
def shout(message):
	message += "!!!!"

hello = "Hello World"
hello = shout(hello)
print(hello)
```

We can store this in a new variable, or we can re-use the same variable name by overwriting it.

Inversely, if you pass in a mutable data type into a function, like a list, you can actually change its contents with the function. You don't have to return it. 

That's because, unlike in the previous example where we get a copy of the data, here we actually get a reference to the original object.

```python

def double_list_values(my_list):
	for i in range(len(my_list)):
		my_list[i] *= 2

original_list = [1, 2, 3]
print(original_list) # [1, 2, 3]

double_list_values(original_list)
print(original_list) # [2, 4, 6]
```

Consider this example where we have a function to double all of the values in a list. Here we don't need to return the doubled list, we can update its values directly within the scope of the function.

And when we use a function to modify something outside the scope of the function, this is called a "side-effect".

## The Power of Abstraction

Now, the major advantage of functions is that they let us build useful abstractions on code that is otherwise not very intuitive to read.

And if you hear the word "abstraction" in software engineering, it means to hide away the complexity of something from a user (and sometimes that user is yourself), and just expose the its key elements.

Basically, it means to simplify something in a really useful way. To me, this is the core value of a function.

Here's an example.

Take a look at this formula. This represents something that is very common, and is probably affecting you right now. Can you tell what it is, or what it does?

```
x * (1 + y) ** z
```

What about if we turn these variable names into something meaningful? 

```python
principal * (1 + rate) ** years
```

Does this help clarify what the formula does? It's calculating the interest for a given principle amount, interest rate, and time period. Like for a bank deposit or a home loan.

If we wanted to use it now, this is how it might look. Better, but still pretty complex.

```python
principal = 1000
rate = 0.05
years = 2
interest = principal * (1 + rate) ** years
```

Let's turn it into a function.

```python
def calc_interest(principal, rate, years):
	return principal * (1 + rate) ** years
```

So that now we want to use it, it's just really straightforward. We went from something that was cryptic to something that most humans will understand just by reading it, even if they don't know how to code.

And I think one of the most important skills for a programmer to have is exactly being able to do this. It's not advanced mathematics or memorising a bunch of algorithms.

But being able to turn complex ideas into simple abstractions, so that we can build big, amazing things from simple parts.

```python
 # Before
x * (1 + y) ** z

 # After
interest = calc_interest(principal=1000, rate=0.05, years=2)
```
