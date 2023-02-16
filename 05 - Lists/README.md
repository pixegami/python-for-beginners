# 05: Lists

Lists in Python are used to store a collection of items in a single variable. You can store numbers, strings, and even other lists.

To create a list, you use square brackets and separate each item you want to add to the list with a comma.

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

This number is called the "index". It corresponds to the position of an item in the list (except that it starts counting at 0).

So `0` here corresponds to the first item, which is an "apple". And `1` corresponds to the second item, which is a "banana".

## List Operations

When creating a list, we don't always know ahead of time what all of its contents are going to be.

So it's quite common to create an empty list, and then be able to add or remove items as our program is running.

Here's how to add items to an existing list:

```python
# Create an empty list
fruit_basket = []

# Add items to a list.
fruit_basket.append("apple")
fruit_basket.append("banana")
fruit_basket.append("carrot")

print(fruit_basket)  # ['apple', 'banana', 'carrot']
```

We can also find out the current length of a list (how many items are in it).

```python
# How many items are in the list?
print(len(fruit_basket))  # 3
```

And you can remove items from a list as well. There's two ways to do this.

### `remove()`

```python
# Remove an item by value.
fruit_basket.remove("banana")
```

This will go through each item in the list and remove the first one it sees with this value. But this is not efficient, precisely because it _has to go through every item_ first to find the one.

### `pop()`

```python
# Remove the list item from a list.
fruit_basket.pop()
```

This removes the _last_ item from the list.

This is the most efficient way to remove an item from the list (if you want to know why, then you'll learn to learn about **data structures and algorithms**, which is out of our scope for this tutorial).

If there is a specific index of an item you want to remove, you can do that too. For example, if I wanted to remove the first item in a list, I can pop the zero-index.

```python
fruit_basket.pop(0)
```

And in addition to removing the item from the list, the pop function also returns the item to you, making it available to use.

```python
fruit_basket = ["apple", "banana", "carrot"]
fruit = fruit_basket.pop()
print(fruit)  # carrot
```

## Built-in List Functions and Syntax Sugar 🍭

So that covers the _basics_ of using a list in Python. There's a lot of in-built functions and shortcuts (syntax sugar) to make working with lists more productive.

> 👉 These "shortcuts" are usually called "syntax sugar" in Python, because they make things easier to write and read, but don't actually change what the code can do.

### Using a Negative Index

You can use a negative number as an index in a list. This starts counting from the end of the list, so the last item has an index of -1, the second to last item has an index of -2 and so on.

```python
my_list = ["apple", "banana", "blueberry"]
print(my_list[-1])  # blueberry
```

### Reversing a List

You can reverse a list with the `.reverse()` method. This won't give you a new list — it will actually modify your existing list in-place.

```python
my_list = [2, 4, 6, 0, 1]
my_list.reverse()
print(my_list)  # [1, 0, 6, 4, 2]
```

### Sorting a List

You can also sort a list (in-place) using the `.sort()` method. This will sort it in ascending order (if your list is numerical) or alphabetical order (if your list are strings).

```python
my_list = [2, 4, 6, 0, 1]
my_list.sort()
print(my_list)  # [0, 2, 1, 4, 6]
```

### Slicing a List ✂️

You can also **_slice_** a list using the square bracket notation. This will give you a new list with the items in the specified range.

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

---

# Coding Exercise 05: Lists

Here's a list of your shopping expenses for the last month. We want to find the amount of the **top 3** biggest expenses (as a new list).

```python
shopping_expenses = [24, 60, 8, 92, 160, 80, 250, 20, 10]

top_3_expenses = []  # TODO: Get the top 3 shopping expenses.
# The result should be [250, 160, 92]
```

Once you've given it a go, check out the [solution here](./solution_05.py).
