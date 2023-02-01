# Operators

## Intro

Hello everyone! Welcome to part 3 of this 12-part Python tutorial series for beginners.

In this video we're going to learn about operators in Python, which allow us to manipulate, assign and compare data.

## Operators

If you add two numbers together this action is called an "operation". And the + symbol is the operator.

```python
result = 5 + 2
print(result)  # 7
```

Operators are special symbols that perform specific actions on our data and our variables. 

And in the context of this line of code, we would refer to these two numbers as "operands."

The concept of "operators" applies to all programming languages, by the way — and not just Python.

### Arithmetic Operators

```python
x + y   # Addition
x - y   # Subtraction
x * y   # Multiplication
x / y   # Division
x // y  # Floor division
x % y   # Modulus
x ** y  # Exponentiation
```

### Arithmetic Operators

There's actually a couple of different types of operators. Let's first take a look at arithmetic operators, which are basically math symbols.

And they work exactly as you'd expect the, You can use them with numbers. So if you remember from the previous chapter, that'll be the float and integer types.

Let's try them out right now, We can go ahead and either clear out your `main.py` or code this all up in a new file if you prefer. It's up to you.

There's Addition. Subtraction. Multiplication. Division.

Multiplication uses this * character in Python, instead of an x. And I'm pretty sure it's the same in all coding languages, And division is a forward-slash.

---

Generally, if you use these operators with integers (whole numbers), the result will also be an integer. If either operand is a float, the result will be a float.

The exception here is division, which will always result in a float, even if the operands are both integers.

---

If you want an integer result from division, you need to use this double-slash operator. This is an integer division, and will round the result down to the nearest whole number.

So those are the most commonly used arithmetic operators in Python.

The less commonly used ones are the exponent operator (a double * , which is when you want to raise something to the power of 2 (or any number).

```python
10 ** 2  # == 100
```

And there's the modulo operator, which is a percent symbol. And it lets you find the remainder of division.

```python
10 % 3  # == 1
10 % 5  # == 0
```
  
Arithmetic operators also have an order of precedence. So in a case like this, the multiplication will be executed before the addition (even though it comes after, if you read it from left to right):

```python
1 + 2 * 3  # == 7
```

But instead of trying to learn and memorise the order of precedence, you could just also just use parentheses (the round brackets) if you want to control the order of execution.

```python
(1 + 2) * 3  # == 9
```

## Assignment Operators

Assignment Operators are how set set values to a variable. So this is both how we can create new variables, or update the value of an existing variable.

(Show example of setting a value, then overwriting it).

## Comparison Operators

Comparison operators are how we check the relationship between two or more values. 

Let's imagine we want to build a personal finance or a personal banking app. We'll need the comparison operator to do things like:

### Uses of Comparison Operator
* 👉  Check user is authorized
* 👉  Check account balance

Checking the name of our user to see if it's someone we recognise. And if they want to withdraw $100, also check if they have enough money in their account.

Here's an example of a comparison operators. This double-equal sign checks for equality.

```python
x = 3
y = 5
print(x == y)
```

And when I run this, it prints False. 

Now the technical term of this thing, is an "expression" (sometimes you'll also hear the term "statement", which is a similar thing). 

It's the lines you see in your editor as you're writing it.

### Expression

```python
x == y
```

Can you tell me right now, just looking at this expression (and nothing else). If this is True or False?

You can't, unless you know the values of x and y at the exact time that this line is evaluated by Python.

When you run this program and you get to this line, Python evaluates this expression with the information it has.

So this is called an "evaluation," and here we can say that at runtime, this statement evaluates to True.

### Evaluation

```python
result = x == y
print(result)  # True
```

Here are a list of all the other comparison operators in Python. You can check if something is equal to, less than, greater than and so on. 

You can also check check for inequality with exclamation mark equals.

Now pay attention because everyone makes this mistake at least once. The assignment operator is different to the equality operator.

The single equal sign is the assignment operator, and that will set or override the value of a variable. It tells Python to do something.

The comparison operator, the double equals sign, checks whether two things have the same value. So they look similar, but they do completely different things. So just keep an eye out for that.

## Logical Operators

And now the last type of operator we'll cover today are logical operators.

Logical operators are used to compare the relationship between two or more Boolean expressions and return a Boolean value of True or False.

### Logical Operators

```python
x and y   # AND
x or y    # OR
not x     # NOT
```

This is to ultimately help our program make decisions.

For example, should I make coffee right now?

```python
# Should I make coffee right now?
is_cup_empty = False
is_daytime = True
should_make_coffee = is_cup_empty and is_daytime
```

Or here's another example. Let's say we're building a travel planning app, and we want it to recommend whether we should walk or drive to a target location.

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

You also have a negation operator, so that's if you want to check whether the opposite of something is true.

```python
is_raining = True
should_bring_umbrella = not is_raining
```

## Wrapping Up

So now I hope you know what operators are in Python, and how you can use them.

See you in the next video, where we're going to look at "conditions" in Python, which lets us control what your code will do, depending on whether a variable or an expression is True or False.