
class NotQuitePrivate(object):
    def __init__(self):
        self._kind_of_private_value = 'something'

    def _sort_of_private_method(self):
        print('This is only supposed to be accessed within the class.')

x = NotQuitePrivate()
print(x._kind_of_private_value)
x._sort_of_private_method()

class NotQuitePrivateProblem(object):
    def __init__(self, n, d):
       self.set_denominator(d)
       self.set_numerator(n)

    def set_numerator(self, n):
        self._n = n

    def set_denominator(self, d):
        if d == 0:
            raise ValueError('D can\'t be zero.')
        self._d = d
    
    def get_quotient(self):
        return self._n / self._d
'''
q = NotQuitePrivateProblem(3, 5)
print(q.get_quotient()) # this works fine, as expected

# this would not work
# q.set_denominator(0)

# but this will!
q._d = 0
q.get_quotient() # which will cause an error here.
'''


class ActuallyPrivate(object):
    def __init__(self, n, d):
       self.set_denominator(d)
       self.set_numerator(n)

    def set_numerator(self, n):
        self.__n = n

    def set_denominator(self, d):
        if d == 0:
            raise ValueError('D can\'t be zero.')
        self.__d = d
    
    def get_quotient(self):
        return self.__n / self.__d

    def __private_method(self):
        print('Only callable inside the class.')


q = ActuallyPrivate(3, 5)

# prints 0.6
print(q.get_quotient())

# This will not work at all - you'll get an error!
q.__private_method()


# This will work... but it doesn't do what you might expect.
q.__d = 0 

# still prints 0.6
print(q.get_quotient())
