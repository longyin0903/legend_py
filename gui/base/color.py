class Color:
  def __init__(self, red, green, blue, alpha = 255):
    self._red = red
    self._green = green
    self._blue = blue
    self._alpha = alpha
  
  def __eq__(self, other):
    if isinstance(other, Color):
      return self._red == other._red and \
             self._green == other._green and \
             self._blue == other._blue and \
             self._alpha == other._alpha
    else:
      raise TypeError("Type mismatch, expect a Color")

  def red(self):
    return self._red
  
  def green(self):
    return self._green
  
  def blue(self):
    return self._blue
    
  def alpha(self):
    return self._alpha
  
  @classmethod
  def from_int(cls, value):
    return cls((value >> 24) & 0x0ff, (value >> 16) & 0x0ff,
               (value >> 8) & 0x0ff, value & 0x0ff)

  def to_int(self):
    return (self._red << 24) | (self._green << 16) | (self._blue << 8) | \
           self._alpha