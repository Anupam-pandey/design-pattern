from abc import ABC

class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return ("A circle of radius {0}".format(self.radius))

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
    # todo
        return ("A square with side {0}".format(self.side))


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape
    
    def resize(self, factor):
        
    # todo
    # note that a Square doesn't have resize()
        if isinstance(self.shape,Square):
            self.shape.side *= factor
        else:
            self.shape.resize(factor)


    def __str__(self):
    # todo
        return ("{0} has the color {1}".format(self.shape,self.color))






print (ColoredShape(Circle(5),"red"))
s = Square(2)
print (s)
s =  ColoredShape(s,"yell")
s.resize(6)
print (s)