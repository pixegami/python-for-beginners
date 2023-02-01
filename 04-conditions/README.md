# Conditions

In this video we're going to learn about conditions in Python, which we can use to control flow of our program based on whether something (like a variable or a statement) is true or false.

So now instead of just executing every line of our program from top to bottom, we can make it execute just some parts and not others by using conditions.

```python
if is_morning:
	print("Let's go for a ☕️")
else:
	print("Let's go for a 🍺!")
```

We can use them together with logical operators and booleans. These are `if/else` statements.

Here's an example of an if statement.

```python
is_raining = True
if is_raining:
	print("It's raining!")
```

If this expression evaluates to `True`, the code in this scope will be executed.

The scope is whatever is indented here under this if condition. It's usually 4 spaces, but in VSCode pressing tab will do that for you.

If the condition is NOT true, this code path will not be executed. And it'll just carry on to the next thing in its scope.

To demonstrate that, we can add another print statement here, unindented. This is no longer in the scope of the `if` condition, so if will print, even when the condition in `False`.

```python
is_raining = False
if is_raining:
	print("It's raining!")

print("Have a nice day!")
```

And now the code path that gets executed will depend on whether it's raining or not.

Notice how we still reach this line at the end no matter which code path gets executed.

That's because it's out of the scope of the condition. And once that condition code is resolved, the Python interpreter moves on to this line.

And if we want something something else to happen when the condition in False, we can use the `else` keyword, like this. So let's take our previous example but now imagine we're building a trip planner, like in Google maps.

And if it's raining we're going to drive. Otherwise we'll take the bicycle.

```python
# Route Planner
is_raining = False
if is_raining:
	print("Drive to Destination")
else:
	print("Cycle to Destination")

```

There is also an "else if" statement, which Python shortens to `elif`. This will execute if the preceding conditions are False.

```python
is_raining = False
distance_kms = 5.0

if is_raining or distance_kms > 10:
	print("🚗 Drive to Destination")
elif distance_kms < 1:
	print("🚶 Walk to Destination")
else:
	print("🚲 Cycle to Destination")
```
