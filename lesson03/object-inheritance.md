# Python Inheritance

## Introduction

This tutorial will discuss inheritance in Python objects. Inheritance allows our objects to be treated as something basic and common, while implementing more specific behaviors. It also allows us to define some common behaviors and reuse them in other objecLet's go!

## Defining a Parent Class

If we wanted to build a code library that was full of shapes, we could do it by definining each shape indvidually. Each one could have its own behavior, its own methods, and its own properties. That might work out fine as long as we were using shapes independently, but we'd run into problems as soon as we want to start working with each one of the shapes generically. By using inheritance, we can define some common methods that all of our shapes can perform.

```py
class Shape(object):

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def get_name(self):
        return None
```

Generally, it's good to make sure that your parent classes don't know anything about their child classes. This allows you to think about more particular behavior in the child classes and keep your parent classes basic.

## Defining a Child Class

Now that we have the `Shape` class, we can use it to define our behavior even further. We've already used the `Shape` class to identify that we'll have a few methods, but our Rectangle can implement specific behavior for these. To create a subclass of another class in Python, you just replace `(object)` with the name of your parent class. This indicates that your class is derived from, or inherits from, the specified parent class.

```py
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def get_name(self):
        return 'Rectangle'

```

## Making It a Bit Simpler

With the current way we've got our classes set up, we could be writing a lot of dummy code for `get_name`. Since we expect this to be the same across all of our instances of `Shape` objects, we can define this method in the `Shape` class. Let's change the `get_name` method and add an `__init__` method, so it looks like this:

```py
class Shape(object):

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def get_name(self):
        return self.name
```

Now, how can we take advantage of this in our Rectangle class? It's simple - we can just use the `super()` method to access the parent class. If we don't do this, then we won't ever set the `name` property, and Python doesn't execute the parent class's `__init__` method directly. 

Note that when we use `super().__init__`, we don't pass the `self` parameter to the method.

```py
class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__('Rectangle')
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

```

Now, if we run the code below, you can see that `get_name` does what we want, even though we did not define this for the `Rectangle` class.

```py
my_rectangle = Rectangle(5, 2)
print(my_rectangle.get_name())
```

## Another Child Class

If we go one step further, we can see how inheriting behaviors can make our code easier and easier to use. A square is a specific type of rectangle where all four sides are the same length; now we can reuse our code to create a `Square` class very easily.

```py
class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

```

While we didn't have to define any behavior here, our `Square` class has inherited proper implementations from its parent. If you run the following code, you'll see that it works just as expected.

```py
s = Square(8)
print('The area is %s.' % s.get_area())
print('The perimeter is %s.' % s.get_perimeter())
```

There's only one problem; we will run into unexpected behavior if we call `get_name`. This is OK, though, as we can fix it in our `__init__` method by simply defining the `self.name` property.


```py
class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.name = 'Square'

```

Now, `get_name` should work as expected.

```py
print(s.get_name())
```

This ability to treat different, specific implementations as a common thing is often referred to as **polymorphism**. Polymporphism allows us to treat different types of objects similarly, and allows a single object to behave in different ways. 

The method below will illustrate this; even though each `Shape` may have different definitions, this code will work for all of them.

```py
def describe_shape(shape):
    print('The area of a %s is %s.' % (shape.get_name(), shape.get_area()))
    print('The perimeter of a %s is %s.' % (shape.get_name(), shape.get_perimeter()))
```