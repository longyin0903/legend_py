class Point:
  def __init__(self, x, y):
    self._x = x
    self._y = y
    
  def __eq__(self, other):
    if isinstance(other, Point):
      return self._x == other._x and self._y == other._y
    else:
      raise TypeError("Type mismatch, expect a Point")
      
  def x(self):
    return self._x
    
  def y(self):
    return self._y
    
  def moveto(self, x, y):
    self._x = x
    self._y = y
       
class Rect:
  class Size:
    def __init__(self, width, height):
      self._width = width
      self._height = height
    
    def __eq__(self, other):
      if isinstance(other, Rect.Size):
        return self._width == other._width and self._height == other._height
      else:
        raise TypeError("Type mismatch, expect a Rect.Size")

    def width(self):
      return self._width
    
    def height(self):
      return self._height
      
    def resize(self, width, height):
      self._width = width
      self._height = height
      
  def __init__(self, left, top, width, height):
    self._position = Point(left, top)
    self._size = Rect.Size(width, height)
  
  @classmethod
  def init(cls, position, size):
    return cls(position.x(), position.y(), size.width(), size.height())
  
  def position(self):
    return self._position
    
  def size(self):
    return self._size

  def left(self):
    return self._position.x()
    
  def top(self):
    return self._position.y()

  def width(self):
    return self._size.width()
    
  def height(self):
    return self._size.height()

  def right(self):
    return self._position.x() + self._size.width()
    
  def bottom(self):
    return self._position.y() + self._size.height()
 
  def moveto(self, x, y):
    self._position.moveto(x, y)
       
  def resize(self, width, height):
    self._size.resize(width, height)
