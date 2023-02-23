# Classes

In this video, we're going to talk "classes" in Python, and this is the last major concept we need to cover in the beginner series.

So what are classes? One way to think about it, is that it is a blueprint for objects that we want to create.

It's also a way of organising code --- grouping the variables and functions that we've learnt about previously) into a unit.

And it's also a form of abstraction. So if you recall, that means turning something complex and ambiguous into a something that's simple and useful to us.

Let's look at an example. Say I'm building a food database for a supermarket. And I want to have information about each food product

```python
class Product:
	
	def __init__(self, name, calories, price_per_kg):
		self.name = name
		self.calories = calories
		self.price_per_kg = price_per_kg
	
```

Now this is the blueprint for the object. It's not referring to a particular house. It's just a way for us to specify what all houses should have.

Now here's how I can use a class to create a specific copy of a house. And a specific, concrete object created from a class is called an 'instance'.

```python
banana = Product("banana", 400, 2.0)
tomato = Product("tomato", 400, 2.0)
potato = Product("potato", 400, 2.0)
```

So here we say that this is an instance of a house. And each instance will have it's own set of values.

## Instance Methods

So we've seen that each instance of a class can have its own set of variables. It can also have it's own functions. And we tend to call this a "method" - even though it's more or less a function.

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

And when I'm using a class method, it's receiving that instance as the "self" variable.

Now it's also possible for me to have variables or functions that are not associated with any particular instance, but with the entire class itself.

So image same global constant. This is going to be the same for all houses, so there's really no need to store a copy of it for each instance of the house. Instead, let's make this a class variable by putting it up here.

```python
class Product:
	CALORIES_TO_KILOJOULES = 4.184
	# ...
	def get_kilojoules(self):
		return self.calories * Product.CALORIES_TO_KILOJOULES
```

In Python convention, we capitalise the names of variables that we don't expect to ever change or have new values once it is defined. And we call these variables "constants".

---

I've just shown you a specific example of how to use a class. But you can use it in many more ways than this:

* A game, and each character is a class with their own health and power values.
* Make an online store, like Amazon. Each class is a product.
* Building a complex road traffic simulation, and each class is one of the pieces in that system - like a vehicle or an traffic light.

---

So that's quick introduction about classes, how to use classes and how to create classes in Python. But it's a subject that goes much deeper than this. 

And if you're keen to learn more about how classes work, then I recommend looking up something called "Object Oriented Programming", which is a programming strategy that revolves heavily around the use of classes.

However, I think what you've learnt here today is enough to get you going and solving problems. 

I also personally tend to use a functional style of programming myself, which doesn't rely using classes much. So that's why I've kept this chapter relatively lightweight.

---
Bank deposit?
Car?
Food?
Geometry?
Game?
Shopping Card?
Food Product?