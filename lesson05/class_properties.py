
class MyFirstClass(object):
    data = []

    def __init__(self, name):
        self.name = name

    def print_it(self):
        print('%s: %s' % (self.name, self.data))


a = MyFirstClass("a")
b = MyFirstClass("b")

a.print_it() # prints a: []
b.print_it() # prints b: []

a.data.append(0) # does a.data contain [0]?
b.data.append(1) # does b.data contain [1]?

a.print_it() # prints a: [0, 1]
b.print_it() # prints b: [0, 1]

print(MyFirstClass.data)


class MySecondClass(object):
    my_number = 0

    def __init__(self, name):
        self.name = name
        self.my_number = 0

    def increment(self):
        self.my_number += 1

    def print_it(self):
        print('%s: %s' % (self.name, self.my_number))

    def print_for_class():
        print(MySecondClass.my_number)


c = MySecondClass('c')
d = MySecondClass('d')

c.print_it() # prints c: 0
d.print_it() # prints d: 0

c.increment()

c.print_it() # prints c: 1
d.print_it() # prints d: 0

MySecondClass.print_for_class() # prints 0

################################################################################