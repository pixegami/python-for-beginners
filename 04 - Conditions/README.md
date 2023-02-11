# 04: Conditions

Conditions in Python are boolean expressions used to control the flow of the program. These expressions usually have a value of either `True` or `False`. 

For example, we could have a variable `is_morning` that is `True` if it is morning and `False` if it is not morning. We could then use this variable in a condition to determine what we should drink:

```python
if is_morning:
	print("Let's go for a ☕️")
else:
	print("Let's go for a 🍺!")
```

We can use them together with logical operators and booleans. These are `if/else` statements.

### `if`

Here's an example of an `if` statement.

```python
is_raining = True
if is_raining:
	print("It's raining!")
```

If this expression evaluates to `True`, the code in this scope will be executed.

### Condition Scope in Python

The scope is whatever is indented (4 spaces) under this `if` condition. If the condition is NOT true, this code path will not be executed. And it'll just carry on to the next thing in its scope.

To demonstrate that, we can add another print statement here, unindented. This is no longer in the scope of the `if` condition, so if will print, even when the condition in `False`.

```python
is_raining = False
if is_raining:
	print("It's raining!")

print("Have a nice day!")
```

And now the code path that gets executed will depend on whether it's raining or not. Notice how we still reach the line at the end no matter which code path gets executed.

### `else`

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

### `elif`

There is also an "else if" statement, which Python shortens to `elif`. This will execute if the preceding conditions are `False`.

For example, let's imagine we want to write some code to decide how to get to a destination.

We have variables for whether it's raining and whether it's far away:

```python
is_raining = False
is_far = False
```

We want to decide whether to drive, walk or cycle to the destination:

```python
if is_raining or is_far:
	print("🚗 Drive to Destination")
else:
	print("🚶 Walk to Destination")
```

In this case, the `else` statement will execute, because neither `is_raining` nor `is_far` are `True`.

But what if we want to also include cycling as an option? We can add an `elif` statement:

```python
is_raining = False
is_far = True

if is_raining or is_far:
	print("🚗 Drive to Destination")
elif not is_far:
	print("🚶 Walk to Destination")
else:
	print("🚲 Cycle to Destination")
```

You can also include conditions with numerical values (and use them together with  comparison operators). For example, if we want to include cycling as an option only if the distance is between 1 and 10 km, we can add an `elif` statement like this:

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
