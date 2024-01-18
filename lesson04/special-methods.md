# Special Methods in Python Objects

## Introduction

Now that we've learned some things about specifying classes, instantiating objects, and how inheritance works in Python, we'll get more into some of the capabilities of objects. In Python, we can use _special methods_ - sometimes called _dunder_ methods or _magic_ methods, to provide additional behaviors beyond setting properties and calling methods.

## Simple Special Methods

We already discussed `__init__`, which is an important method that is used to instantiate an object. There are a few other very common special methods. One really common one:

* `__str__(self)` can be used when an object needs to be converted to a string. For example, when calling `print(my_object)`.

For many objects, it's a good idea to implement this special method, as it makes it possible to insert this object into a string - and can be very useful for your own debugging purposes.


## List Special Methods

There are many more than just `__init__` and `__str__`. For example, there are many special methods so that you can treat your object like a list.

* `__getitem__(self, index)`: this allows you to access values in your object with an index, like with a list. For example, you can retrieve the first value in your list-like object with `my_object[0]`. Note that you can also this approach to make your object operate like a dictionary.
* `__setitem__(self, index, value)`: very similar to `__getitem__`, this allows you to set values in your object with an index. 
* `__len__(self)` can be used when an object is passed to the `len()` function. This is useful in list-like objects.
* `__contains__(self, item)` is used with the `in` keyword. Again, if `my_object` is kind of like a list and you want to know if `thing` is in it, you can implement `__contains__` and then use `thing in my_object` in your Python code.

This example illustrates a special type of list object that can only accept / output boolean values. By implementing the special methods above, we can treat it like a Python list. Review this code so you can see some examples of implementing and using these methods.

```bash
edit bitlist.py
```

You might have good reason to wrap a Python list in an object - either for type safety or for other requirements. These methods allow you to build objects that can suit a lot of different purposes, and often this can lead to safer or more predictable code.


## Operator Special Methods

Beyond list special methods, there are also operator overrides. In some languages, implementing support for operators like `+`, -``, and `*` is challenging (if it's possible at all). In Python, it's as simple as using a special method. Note that all of these methods should return a value.

* `__add__(self, other)`: support for `my_object + other`.
* `__sub__(self, other)`: support for `my_object - other`.
* `__mul__(self, other)`: support for `my_object * other`.
* `__div__(self, other)`: support for `my_object // other`.
* `__truediv__(self, other)`: support for `my_object / other`.
* `__neg__(self, other)`: support for `-my_object`.
* `__pow__(self, other)`: support for `my_object ** other`.

Note that while these operators are often mathematical, they are not **required** to be. They can be used for several reasons - for example, when used with lists, the lists are combined.

The following example implements a rational number; this is really just a fraction. It will allow you to define fractions, add them, subtract them, multiply them, and divide them. Review the code so you can see the implementation and how these methods are used.

```bash
edit rational_num.py
```

By intelligently using operators, you can make your code more readable and provide lots of capabilities to anyone who might need to use your code in the future.


## Even More Special Methods

There are many special methods. You can find a list here: [https://docs.python.org/3/reference/datamodel.html#special-method-names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
