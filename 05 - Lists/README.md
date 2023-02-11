# Lists

In this video we're going to learn about lists in Python. A list is a data structure that allows us to store and work with a lot of data at once.

So far we've only been dealing with single, individual prices of data.

But in the real world, it's far more common to have data that appears as part of some collection or sequence.

This could be a collection of items stocked by an e-commerce retailer. Or, sequential episodes of a Netflix show. Items in an adventure game.

Or in our banking app example, the transactions of an account.

To deal with these situations, we can use a list in Python. In other programming languages, you may also see it being referred to as "arrays" or "vectors".

In Python we call them "lists", and lists are a collection of variables. And we can create one by using these square brackets.

Here's an example of a list like this.

```python
# How to create a list.
fruit_basket = ["apple", "banana", "carrot"]
```

And because a list is sequential, the order we put things into a list matters.

And you can access any of the items in a list, by using the square brackets as well. So type variable of the list, square brackets, then number of the item you want to access.

```python
# How to create a list.
fruit_basket = ["apple", "banana", "carrot"]

# Accessing the items in a list.
print(fruit_basket[0])  # "apple"
print(fruit_basket[1])  # "banana"
```

This number is called the "index". It corresponds to the position of an item in the list, except that it starts counting at 0.

So 0 here corresponds to the first item, which is an "apple". And 1 corresponds to the second item, which is a "banana".

### List Operations

When creating a list, we don't always know ahead of time what all of its contents are going to be.

So it's quite common to create an empty list, and then be able to add or remove items as our program is running

```python
# Create an empty list
fruit_basket = []

# Add items to a list.
fruit_basket.append("apple")
fruit_basket.append("banana")
fruit_basket.append("carrot")
```

We can also find out the current length of a list (how many items are in it).

```python
# How many items are in the list?
print(len(fruit_basket))  # 3
```

And you can remove items from a list as well. There's two ways to do this.

```python
# Remove an item by value.
fruit_basket.remove("banana")
```

This will go through each item in the list and remove the first one it sees with this value. But this is not efficient, precisely because it has to go through every item first to find the one.

Another way to items from a list is:

```python
# Remove the list item from a list.
fruit_basket.pop()
```

This removes the last item from the list. This is the most efficient way to remove an item from the list.

If you want to know why, then you'll learn to learn about data structures and algorithms, which is out of our scope for today.

If there is a specific index of an item you want to remove, you can do that too. For example, if I wanted to remove the first item in a list, I can pop the zero-index.

```python
fruit_basket.pop(0)
```

And in addition to removing the item from the list, the pop function also returns the item to you, making it available to use.

So you can use it like this.

```python
fruit_basket = ["apple", "banana", "carrot"]
fruit = fruit_basket.pop()
print(fruit)  # carrot
```

### List Syntax Sugar

So that covers the _basics_ of using a list in Python. There's a lot of in-built functions and shortcuts to make working with lists more productive.

Let's run through them quickly.

### Using a Negative Index

```python
my_list = ["apple", "banana", "blueberry"]
print(my_list[-1])  # blueberry
```

### Reversing a List

```python
my_list = [2, 4, 6, 0, 1]
my_list.reverse()
print(my_list)  # [1, 0, 6, 4, 2]
```

### Sorting a List

```python
my_list = [2, 4, 6, 0, 1]
my_list.sort()
print(my_list)  # [0, 2, 1, 4, 6]
```

### Slicing a List

```python
my_list = [2, 4, 6, 0, 1]
sliced_list = my_list[0:3]
print(my_list)  # [2, 4, 6]
```

```python
# You can also use this without the index.
# This will just silence from the beginning of the list to index 3.
my_list[:3]

# Or from index 3 to the end of the list.
my_list[3:]
```

```python
# Slice (clone) the entire list.
cloned_list = my_list[:]
```
