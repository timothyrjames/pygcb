import math

class Shape(object):

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def get_name(self):
        return self.name


def describe_shape(shape):
    print('The area of a %s is %s.' % (shape.get_name(), shape.get_area()))
    print('The perimeter of a %s is %s.' % (shape.get_name(), shape.get_perimeter()))


# Your code below

class Triangle(Shape):
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height =height

    def get_perimeter(self):
        perimeter= self.length + self.width + self.height
        return perimeter

    def get_area(self):
        s = (self.length +self.width + self.height)/2
        area = math.sqrt[s(s-self.length)(s-self.width)(s-self.height)]
        return area

    def get_name(self):
        return Triangle
        

             
    
    
