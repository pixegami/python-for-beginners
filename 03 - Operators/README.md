# 03: Operators

Operators are special symbols that perform specific actions on our data and our variables. Here's an example of us adding two numbers together, where `+` is the operator:

```python
result = 5 + 2
print(result)  # 7
```

And in the context of this line of code, we would refer to these two numbers (5 and 2) as "operands." The concept of "operators" applies to all programming languages, — not just Python.

## Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations on numbers. Here are the most common arithmetic operators in Python:

```python
x + y   # Addition
x - y   # Subtraction
x * y   # Multiplication
x / y   # Division
x // y  # Floor division
x % y   # Modulus
x ** y  # Exponentiation
```

Generally, if you use these operators with integers (whole numbers), the result will also be an integer. If either operand is a float, the result will be a float. For example:

```python
print(5 + 3)  # 8
print(5 - 3)  # 2
print(5 * 3)  # 15
```

The exception here is division, which will always result in a float, even if the operands are both integers.

```python
print(5 / 3)
# 1.6666666666666667
```

### Integer Division

If you want an integer result from division, you need to use the `//` operator. This is an integer division, and will round the result down to the nearest whole number.

```python
print(5 / 3)
# 1
```

### Exponent and Modulo Operators

The less commonly used ones are the exponent operator (a double * , which is when you want to raise something to the power of 2 (or any number).

```python
10 ** 2  # == 100
```

And there's the modulo operator, which is a percent symbol. And it lets you find the remainder of division.

```python
10 % 3  # == 1
10 % 5  # == 0
```

Modulo operations are useful when you want to check if a number is divisible by another number, or you have a "wrap around" situation you want to solve (e.g. converting 24h clock into 12h time).

## Order of precedence

Arithmetic operators also have an order of precedence. So in a case like this, the multiplication will be executed before the addition (even though it comes after, if you read it from left to right):

```python
1 + 2 * 3  # == 7
```

The order of operator precedence in Python is:

1. Parentheses
2. Exponentiation
3. Multiplication and Division
4. Addition and Subtraction

But instead of trying to learn and memorise the order of precedence, you could just also just use parentheses (the round brackets) if you want to control the order of execution.

```python
(1 + 2) * 3  # == 9
```

## Assignment Operators

Assignment Operators are how set set values to a variable. So this is both how we can create new variables, or update the value of an existing variable.

```python
x = 2
# x is now 2

x = 4
# x is now 4
```

You can also combine the `=` assignment operator with arithmetic operator to [insert]

```python
x = 2
x += 2
# x is now 4

x *= 2
# x is now 8
```

## Comparison Operators
  
Comparison operators are how we check the relationship between two or more values. Let's imagine we want to build a food ordering app in Python. 

We'll need comparison operators to do things like:

- Check if the user's order is above the minimum order amount 
- See if the item they ordered is available in their location 
- See if the user's order matches the restaurant's inventory 

We can use comparison operators to compare values and determine if they match or not. Here's a list of common comparison operators in Python:

```python
==  # Equals
!=  # Not Equals
<   # Less Than
>   # Greater Than
<=  # Less Than or Equal To
>=  # Greater Than or Equal To
```

Here's an example of using the equality comparison operator.

```python
x = 3
y = 5
print(x == y)  # False
```

### Expression

The technical term for a line like this in Python, is an "expression"

```python
x == y
```

An expression is a combination of values, variables, operators, and/or functions that results in a single value. In this case, the expression is a comparison operator that checks if the value of x is equal to the value of y.

You won't know the result of this expression just by looking at this line on its own, unless you know the values of x and y at the exact time that this line is *evaluated* by Python.

When you run this program and you get to this line, Python evaluates this expression with the information it has.

### Evaluation

```python
result = x == y
print(result)  # True
```

An "evaluation" in Python is the process of interpreting an expression and determining its value. In this example, the expression is `x == y` and the result of the evaluation is either `True` or `False`.

So here in this example, we can say "the expression evaluates to `True`".

## Logical Operators

Logical operators are used to compare the relationship between two or more Boolean expressions and return a Boolean value of True or False.

### Logical Operators

```python
x and y   # AND
x or y    # OR
not x     # NOT
```

This is to ultimately help our program make decisions. For example, should I make coffee right now?

```python
# Should I make coffee right now?
is_cup_empty = False
is_daytime = True
should_make_coffee = is_cup_empty and is_daytime
```

Here's another example. Let's say we're building a travel planning app, and we want it to recommend whether we should walk or drive to a target location.

```python
# Should I walk or drive to my destination?
is_raining = False
is_far = True
should_drive = is_raining or is_far
```

Now you can combine these operators and these expressions to create really complex rules systems. So like in this previous example, how can I well whether  something is far away?

```python
is_raining = False
is_far = distance_meters > 1000
should_drive = is_raining or is_far

# Same as inlining it.
should_drive = is_raining or (distance_meters > 1000)
```

You also have a negation operator (`not`), so that's if you want to check whether the opposite of something is true.

```python
is_raining = True
should_bring_umbrella = not is_raining
```
