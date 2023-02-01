# Loops

In this video we're going to learn about loops in Python. Loops are a way of repeating the execution of our code.

And there's several different ways to do this. We can repeat for a fixed number of times, like counting to 100.

Or if we have a list of items, we can go through each item and do something with it. Like calculating the total checkout price of a shopping cart.

Or we can also just keep repeating a loop forever as long as a certain condition is True. Like if we're making a game, we can run the code in loop until the player quits.

### 🔄 Uses of Loops

- Repeat for X number of times
- Repeat for all items in a collection
- Repeat while a condition is "True"

## Using Loops with Lists

Now that you know how to work with lists and individual items in a list, let's first look at how a loop would be useful there.

What if we wanted to do something with all of the items in a list, one by one?

Imagine we developing a poker game, and wanted to calculate our odds of winning based on the cards in our hand.

Or if we wanted to work out the overall account balance from a list of transactions.

We need a way to go through items in a list one-by-one, so that we can do something with each of the items — whether there's just summing up a transaction amount, or calculating the odds of a winning poker hand.

In programming, the concept going through something step-by-step is called _iteration_. And we can use a "loop" to iterate through the items in a list.

## For Loops

This is how we can write a loop in Python. And this is called "for" loop because of the "for" keyword here.

```python
fruit_basket = ["apple", "banana", "blueberry"]
for fruit in fruit_basket:
	print(f"There is a {fruit} in the basket!")
```

And translating this into human language, it's basically saying "for each item in this collection of items", I want to run this piece of code.

So this piece of code is going to run three times, since there's three items in our list.

The first time this runs, the "fruit" will be "apple". In the next iteration, it's equal to "banana" and so on.

## Enumerate

Sometimes, when you do a loop, it's also useful to know the index of the item that we're currently iterating on.

We can use the built-in `enumerate()` function to do that. Wrap this function around our list variable. And now, we have an additional variable we can use, that will tell us the index of the iteration.

You can all this variable anything you want, but in programming convention, we tend to use the letter "i" which can stand for "iteration" or "index".

```python
fruit_basket = ["apple", "banana", "blueberry"]
for i, fruit in enumerate(fruit_basket):
	print(f"There is a {fruit} in the basket at index {i}!")
```

## For In Range

What if we don't care about a particular list, and we just want to run a piece of code 10 times?

We can use a for loop to do that as well. We'll just use this in-built range function. And this will loop 10 times.

```python
for i in range(10):
	print(f"Running: {i} time")
```

And the "range" function is actually quite flexible, so if you want to see what else it can do, I recommend taking a look at the official Python documentation for this function.

## While Loops

So we've just covered "for" loops, which is useful for iterating through a list, or a range of numbers.

But there's another type of loop available in Python as well, and this is called a 'while' loop.

The difference is that, instead of iterating for a fixed range, the "while" loop iterates based on some condition. And it will continue to iterate as long as that condition is true.

For example, you might have heard the term "game loop" in reference to video games. It's the game code that runs in a loop as long as the player is still playing.

In our banking app example, this type of loop is useful for when we want the user's input. We want the app to prompt the user for input, until we get a valid response.

And if we don't, instead of crashing, we should loop back to the beginning of the input flow and prompt them again.

A while loop in Python looks like this. We use the keyword 'while' and then follow it with an expression.

As long as the expression evaluates to true, this code will keep executing.

```python
while True:
	print("This will loop forever!")
```

So if I actually run this right now, my program will be stuck running forever. This is called an infinite loop, and it's usually a bug.

If you accidentally do this, you can force exit your Python interpreter by pressing `Ctrl + C` in your terminal.

## Break and Continue

You can also terminate a loop from within using the `break` keyword. So this will now cause the loop to run once, before we break out of of it.

```python
while True:
	print("This will loop forever!")
	break
```

And we can combine this with the other things we've learnt so far, to make the loop break when certain conditions are met.

For example, let's keep track of how many times this loop is run, and break on the 5th iteration.

```python
count = 0
while True:
    count += 1
	print(f"This has run {count} times!")
	if count == 5:
		break
```

Another useful keyword to know is the `continue` keyword. So rather than breaking out of the loop entirely, this will just tell Python to go back to the beginning of the loop, and continue with the next iteration.

```python
count = 0
while True:
    count += 1

	if count == 3:
		continue

	print(f"This has run {count} times!")
	if count == 5:
		break
```

To demonstrate that, I can use the `continue` keyword here, when the count is equal to three.

When it reaches this keyword, the loop will stop what it's doing - so it won't reach the rest of this code. And it'll go back to the beginning of the loop and start it again from there.

These two keywords also work with the for-loops we looked at earlier. Here's the exact same code, written as a for loop instead of a while loop.

```python
for i in range(10):
	if i == 3:
		continue

	print(f"This has run {count} times!")
	if count == 5:
		break
```

And finally, the conditional expression in a while loop - this part here, is evaluated fresh each time the loop is run.

Which means that instead of writing "True" to make the loop run forever, we can just write the actual condition there instead.

```python
count = 0
while count < 5:
    count += 1
	print(f"This has run {count} times!")
```

## List Comprehensions

Now "List Comprehensions" are a bit of an advanced topic and it's quite unique to Python, so we're not going to go too far into this.

But I'll just provide a quick summary.

```python
my_list = [2, 4, 6, 0, 1]
new_list = [2 * x for x in my_list]
print(new_list)
```

This is an example of what list-comprehension looks like, in case you see it in the wild.

It's a shortcut for looping through a list, and creating a new list at the same time. In this example, I'm creating a new list where each element is doubled from the original list.

Now we don't need to use the fancy syntax to do this. You can achieve the same thing by writing it out normally.

```python
my_list = [2, 4, 6, 0, 1]
new_list = []
for x in my_list:
	new_list.append(x * 2)
print(new_list)
```

But the list-comprehension technique just makes it a bit faster to write, and a bit easier to read.

Python is full of shortcuts like this, and we call that "syntax sugar."
