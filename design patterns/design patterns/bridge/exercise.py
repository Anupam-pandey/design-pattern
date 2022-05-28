from abc import ABC

class Shape:
    def __init__(self,name,Renderer):
        self.name = name
        self.Renderer = Renderer
    
    def __str__(self):
        return f'Drawing {self.name} as {self.Renderer.what_to_render_as}'



class Triangle(Shape):
    def __init__(self,Renderer):
        super().__init__(name= "Triangle", Renderer= Renderer)
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self,Renderer):
        super().__init__(name= "Square", Renderer= Renderer)
        self.name = 'Square'



# class VectorSquare():
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         print ("hi ")
#         return f'Drawing {self.name} as lines'


# class RasterSquare():
#      def __init__(self,name):
#         self.name = name
#      def __str__(self):
#         print ("bye ")
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

class Renderer(ABC):
    @property
    def what_to_render_as(name):
        return None


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(name):
        what_to_render_as = "pixels"
        return what_to_render_as

class VectorRenderer(Renderer):
    @property
    def what_to_render_as(name):
        what_to_render_as = "vector"
        return what_to_render_as






if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    square = Square(raster)
    # print (type(raster))
    # #print(raster.what_to_render_as())
    print (square)
    # square = Square(vector)
    # print (square)
    #print (vector.what_to_render_as())