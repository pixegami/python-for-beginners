# 07: Dictionaries

Dictionaries are a **data structure** that stores key value pairs. It's similar to a [list](../05 - Lists/) in that it lets us store a collection of data, except instead of relying on insertion order or an index to access individual items, we use a an arbitrary key (for example, a string like `"user_id"`).

A **key** is a unique identifier that we can use to access a value in the dictionary.

## Dictionary vs List

Lists are good at storing sequential data. The index starts at 0, and goes up by 1 for each item. But what if we wanted to store user logins?

If I try to log in with a user name like "Jack", how would I look that up in a list? I could go through each item, and check if my user ID is there.

But if this list had 1 million users, I'm doing a lot of extra work to look that up.

Dictionaries are similar to lists in that they let us store data and access it with square brackets. But instead of an ordinal index (ordinal means integers in a sequence), a dictionary uses a "key", which could be anything—a string, a number, or even more complex things.

If we know the key, we can look up the value of that key instantly, without having to go through every other entry.

## Dictionary Example

```python
fruit_prices = {
	"apple": 0.99,
	"banana": 2.50,
	"blueberry": 3.00
}
```

If we have the key for the item that we want to access, we can use the square brackets to access that value instantly.

```python
print(fruit_prices["apple"])
```

And this is useful if our data doesn't have any kind of ordering in it's relationship, but we know something unique and specific about the item we want to access.

## Adding Elements to a Dictionary

And you can't append things to a dictionary like you do with a list, but you can add new entries to it either using the assignment operator like this, or by using the 'update' function.

```python

fruit_prices["watermelon"] = 5.00
fruit_prices.update("cherry", 4.00)

print(fruit_prices)
# {''watermelon': 5.0, 'cherry': 4.0}
```

## Accessing keys that don't exist

If you try to access a key in the dictionary that isn't there, you'll get a **KeyError** and your program will crash.

You have two options to avoid doing that. You can first check if a key exists inside a dictionary using the `in` keyword.

```python
if "kiwi" in fruit_prices:
	print(fruit_prices["kiwi"])
else:
	print("Didn't find a kiwi!")
```

Or you can use the in-built `get()` function like this.

```python
kiwi_price = fruit_price.get("kiwi")
print(kiwi_price)  # None
```

And if the value doesn't exist, it'll just return `None`. Or if you prefer you specify a default value for it to return instead.

```python
kiwi_price = fruit_price.get("kiwi", 0)
print(kiwi_price)  # 0
```

## Dictionary Built-In Methods

Many of the things you can do with a list, you can also do with a dictionary. For instance, you can get the length of a dictionary using the `len()` function, which will tell you how many items are in there.

```python
fruits = {"banana": 2, "apple": 3, "kiwi": 4}
print(len(fruit_price))  # 3
```

Dictionaries also have their own methods, which you can use to manipulate the data they contain.

```python
fruits.clear()  # Removes all items from the dictionary
fruits.get("apple")  # Gets the value of a key
fruits.items()  # Returns a list of key-value pairs
fruits.keys()  # Returns a list of all keys
fruits.pop("apple")  # Removes an item from the dictionary
fruits.update({"apple": 3})  # Adds or updates existing elements
fruits.values()  # Returns a list of all values
```

## Looping A Dictionary

Just like a list, you can also iterate through a dictionary using a for-loop.

```python
for key in fruit_prices:
	print(key)
	print(fruit_prices[key])
```

This loop might not run in the same order that the items were inserted in.

Dictionaries are an unordered data-structure, which means there's no concept of a 'first item' or a 'last item' in this collection. Just items.

> 👉 Another important detail is that, when you write a loop like this, you actually get the "key" of each item in the dictionary. You don't actually get the **_value_** that it stores. To get that, you'll need to use the key to access that item.

If you do want both the keys and the values available to you each iteration of the loop, you can use this in-built `items()` method.

```python
for key, value in fruit_prices.items():
	print(key)
	print(value)
```

## Dictionary As Objects

The data inside a dictionary doesn't all have to be the same type either. Another way to use it is to store different pieces of data about a single object.

```python
nike_shoes = {
	"name": "Nike AirMax 2020",
	"colors": ["red", "white", "black"],
	"price": 129.99
}
```

And then I can access specific pieces of information about it.

In fact, by this point in the tutorial, you'll have learnt enough about data-types and data-structures to be able to **represent probably 99% of all things in the internet**. Data being sent back and forth on all of these giant tech websites can actually be represented as a dictionary.

The problem though is that "dictionaries" are a Python concept. So how do we communicate data like this to other systems that don't use Python?

## JSON Serialisation

We do that by turning into a format that almost everybody understands. That process is called "serialisation".

And with dictionaries, it can serialise nicely into something called **JSON**, which stands for **Javascript Object Notation**.

And JSON data is everywhere. It's pretty much how a large part of how apps communicate with each other via the internet.

But don't worry about that just yet. All you need to know at this point is Python dictionaries work quite well as JSON data. And Python has easy ways to convert to and from JSON data.

```python
import json
fruit_prices = {"apple": 90}
json_fruit_prices = json.dumps(fruit_prices)
print(json_fruit_prices)
```

# Coding Exercise 07: Dictionaries

Imagine you are making an online expense tracking app, and you are using a dictionary to store the total expenses for things you buy.

```python
total_expenses = {
    "food": 40,
    "transport": 0,
    "shopping": 190
}

# TODO: Add an "entertainment" expense ($20)
# TODO: Increase "food" expense (by $12)
```

You want to add a new item to the dictionary - an "entertainment" expense of $20. You also spend an addition $12 on food and want to update the dictionary.

Fill in the code that updates the dictionary. Once you've given it a go, check out the [solution here](./solution_07.py).
