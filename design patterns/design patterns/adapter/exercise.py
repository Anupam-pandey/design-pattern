class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height


class Rectangle:
    def __init__(self, height=0,width=0):
        self.height = height
        self.width = width

class SquareToRectangleAdapter:
    def __init__(self, square):
        # TODO
        self.height = square.side
        self.width = square.side
        Rectangle(square.side,square.side)
        square  = Square(0)
        #calculate_area(rectangle)
        
        