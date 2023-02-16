# 08: Tuples and Sets

## Tuples

Tuples in Python are immutable sequences of elements. This is what the syntax looks like:

```python
# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)
```

It is similar to a list that we saw earlier. And we can even access its elements in the same way.

```python
 # Access an element of tuple
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
```

The difference is that, after a tuple is created, its **elements cannot be changed**. You can't add, remove, or update elements in tuple.

So far it just sounds like a worse version of a list. So why should we use it? Well it turns out that there's some advantages.

## Tuples vs Lists

- ✅  More efficient
- ✅  Can be used as keys in a dict
- ✅  Safer due to immutability

They are faster and use less memory than lists, making them more efficient for large data sets. They **can be used as keys in dictionaries**, while lists cannot.

```python
my_dict = {(1,2): "value"}
```

They are safer to use in a **multi-threaded environment**, as they cannot be changed by another thread once created.

They can be used to define **multiple return values for a function**, making the code more readable and easier to understand.

And, if we know the size a tuple beforehand (which we usually will), we can also unpack it into separate variables directly, instead of using the index to access it.

This technique is called "unpacking" or "spreading", and is another example of Python's syntax sugar.

```python
 # Instead of this...
my_tuple = (1, 2, 3)
x = my_tuple[0]
y = my_tuple[1]
z = my_tuple[2]

 # We can do this!
x, y, z = (1, 2, 3)
print(x, y, z)
```

Because of this, it's actually common for Python functions to return a tuple as a data-type. We've actually be using examples of this already. 

Remember the items function when we are iterating through a dictionary? That was us unpacking a tuple.

```python
for key, value in fruit_prices.items():
	print(key)
	print(value)
```

## Sets

Sets are another very useful data-structure. They are unordered collections of items, and are mutable. Sets are useful for membership testing, removing duplicates, and mathematical operations like union, intersection, difference, and symmetric difference.

Here is an example. You can create one with the curly braces. Similar to a dictionary—except with just the keys, and no associated value. The key ***is*** the value.

```python
# Create a set.
favorite_fruits = {"🍊", "🍒", "🍌", "🫐", "🍉"}
```

```python
# Create an empty set.
favourite_vegetables = set()
```

Sets are a collection of *unique* elements. They are similar to lists or tuples, but with the major difference that all elements in a set are *unique*. **You can't have two of the same element inside a set.**

Sets come with in-built functions to add or remove elements. And if you try to add something that's already in the set, then nothing will happen.

```python
favorite_fruits = {"🍊", "🍒", "🍌", "🫐", "🍉"}

favorite_fruits.remove("🍌")  # Will be removed
favorite_fruits.add("🥝")     # Doesn't exist, will be added
favorite_fruits.add("🍒")     # Already exists, will be ignored

print(favorite_fruits)
# Output: {'🍒', '🍉', '🍊', '🥝', '🫐'}
```

So what are sets useful for? What problem does it solve for us? Well, let's look at some examples.

## Set Built-In Methods

It's really easy to check if something belongs inside a set. It's also easy to check for ***overlaps or intersections*** with other sets.

For instance, let's say I have a set of my favourite fruits. I can use this expression to check if a blueberry is part of my favourite fruits. And in this case, it is, so this expression will evaluate to True.

```python
favorite_fruits = {"🍊", "🍒", "🍌", "🫐", "🍉"}

print("🫐" in favorite_fruits)  
# True
```

Now let's say I have another set, of fruits that are red in color. And I want to find where the fruits there overlap with my favourite fruits.

Or in other words, my favourite fruits which are also red. This is called an `intersection` of two sets, and I can use it like this:

```python
favorite_fruits = {"🍊", "🍒", "🍌", "🫐", "🍉"}
red_fruits = {"🍎", "🍓", "🍒", "🍉"}
favourite_red_fruits = favorite_fruits.intersection(red_fruits)

print(favourite_red_fruits)
 # {'🍒', '🍉'}
```

There's also the `union` method, which combines all elements in both sets.

```python
 # You can find the union (all members) of two sets.
all_fruits = favorite_fruits.union(red_fruits)
print(all_fruits)
 # {'🍒', '🍉', '🍎', '🍓', '🍊', '🍌', '🫐', '🍋'}
```

And finally there's also the difference method, which finds the elements that appear in either of the sets, but not both.

```python
 # You can find the difference (members in one set but not the other) of two sets.
favorite_fruits_but_not_red = favorite_fruits.difference(red_fruits)
print(favorite_fruits_but_not_red)
 # {'🍊', '🍌', '🫐', '🍋'}
```

# Coding Exercise 08: Tuples and Sets

You are creating an application that helps your user find a restaurant according to their food preferences.

You have a set of your user's favourite foods, and sets of food being served at each restaurant. **Find the restaurant that best matches your user's food preferences.**

```python
food_preference = {"🍔", "🍕", "🍤"}

restaurants = {
    "seafood_cove": {"🍤", "🍣", "🐟", "🦀"},
    "hungry_jacks": {"🍔", "🍟", "🍦", "🍕"},
    "potting_shed": {"🥦", "🥕", "🍞", "🥑"},
}

# Result should be hungry_jacks with {'🍔', '🍕'} being matched.
```

Here you'll also need to apply the knowledge of dictionaries and loops that you learn from previous chapters!

Once you've given it a go, check out the [solution here](./solution_08.py).
