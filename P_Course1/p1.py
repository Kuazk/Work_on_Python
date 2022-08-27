
class rectangle:
    
    def __init__(self,width,height):
        self._width= width
        self._height = height
        
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if value <= 0: 
            raise ValueError("width must be positive")
        else:
            self._width = value
    def __str__(self): 
        return f'rectangle with _width of {self._width} and _height of {self._height}'
    def __repr__(self): 
        return str(self)
    def __eq__(self,other):
        return (self._width == other._width and self._height == other._height)if isinstance(other,rectangle)else False
rec = rectangle(10,20)

rec._width = -10
print(rec)





        