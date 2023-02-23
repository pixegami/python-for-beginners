# 11: Classes

In this chapter we're going to learn about "classes" in Python, and this is the last major concept we need to cover in the beginner series.

So what are classes? One way to think about it, is that it is a blueprint for objects that we want to create.

It's also a way of organising code — grouping the variables and functions that we've learnt about previously) into a cohesive unit, so that we all the things we care about in one place, for convenience.

And it's also a form of abstraction. So if you recall, that means turning something complex and ambiguous into a something that's simple and useful to us.

Let's look at an example. Say I'm building a food database for a supermarket. And I want to have information about each food product

```python
class Product:
	
	def __init__(self, name, calories, price_per_kg):
		self.name = name
		self.calories = calories
		self.price_per_kg = price_per_kg
	
```

Now this class is the blueprint for the product. It's not referring to a *particular* product. It's just a way for us to specify what all products should have.

Now here's how I can use a class to create a specific copy of a product. 

And a specific, concrete object created from a class is called an 'instance'.

### Instances

```python
banana = Product("banana", 105, 1.0)
tomato = Product("tomato", 22, 2.1)
potato = Product("potato", 162, 0.9)
```

So here we say that these are instance of a product. And each instance will have it's own set of values.

```python
print(banana.calories)  # 105
print(banana.tomato)  # 22
```

## Instance Methods

So we've seen that each instance of a class can have its own set of variables. It can also have it's own *functions*. And when a function is part of a class, it's generally referred to as a "method" (by convention).

It's no different from a function though—it more or less works the same way.

Here's how to write one.

```python
class Product:

	# ...
	
	def get_price(self, weight):
		return self.price_per_kg * weight
```

It's got to be in the scope of the class. And the first argument is always a "self" argument, just like these variables here. That's how we actually refer back to them and can manipulate them.

```python
banana.get_price(0.2)
tomato.get_price(0.5)
```

And when I'm using an instance method, it's receiving that instance as the "self" variable.

## Class Attributes

Now it's also possible for me to have variables or functions that are not associated with any particular instance, but with the entire class itself.

For example, if you have a class that deals with food nutrition, it might be helpful to store a constant that holds the conversion factor from calories to kilojoules.

This is a constant that will never change and will be true for all instances of the class, so we could define it like this:

```python
class Product:
	CALORIES_TO_KILOJOULES = 4.184
	# ...
	def get_kilojoules(self):
		return self.calories * Product.CALORIES_TO_KILOJOULES
```

In Python convention, we capitalise the names of variables that we don't expect to ever change or have new values once it is defined. And we call these variables "constants".

## Class Methods

Now let's extend our food product class with a static method.

A static method is a type of method that is bound to the class itself, not the instances of the class.

For example, let's say that we wanted to create a static method on our `Product` class that is used to generate a unique id for new product instances. We would define the static method like this:

```python
import uuid

class Product:
	@staticmethod
	def generate_unique_id():
		return uuid.uuid4()
```

Now we can call this static method on the class itself, like this:

```python
product_id = Product.generate_unique_id()
```

We don't need to create an instance of the `Product` class in order to call this method — we can simply call it directly on the class itself.

---

So you've just seen a specific example of how to use a class in Python. But you can use it in many more ways than this to represent things about the world.

## Uses of Classes

- 👉  Character in a Game
- 👉  Products in a Shop
- 👉  Animals in a Zoo
- 👉  Books in a Library

## Object Oriented Programming

So that's been quick introduction about classes, how to use classes and how to create classes in Python. But it's a subject that goes much deeper than this. 

And if you're keen to learn more about how classes work, then I recommend looking up something called "Object Oriented Programming", which is a programming strategy that revolves heavily around the use of classes.

However, I think what you've learnt here today is enough to get you going and solving problems. 

I also personally tend to use a functional style of programming myself, which doesn't rely using classes much. So that's why I've kept this chapter relatively lightweight.

# Coding Exercise 11: Classes

You're creating a game where the player will have to fight monsters. The game will feature different types of monsters, and each monster will have different stats and abilities.

Create a class called "Monster" that will keep track of the following information:

- ✏️  Health Points
- ✏️  Attack Points
- ✏️  Method to "Fight"

The Monster class should also have a `fight()` method which will allow the monster to attack another monster.

```python
class Monster:
	def __init__(self):
		pass

	def fight(monster):
		pass
```

When you've had a go, see the [solution here](./solution_11.py).