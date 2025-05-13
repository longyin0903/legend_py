class Font:
  def __init__(self):
    self._font = dict()
    
  def load(self, path):
    self._path = path
    for size in [16, 32, 48]:
      self._font[size] = self.load_impl(path, size)

  def default(self):
    return self._font[16]
    
  def get(self, size):
    if not size in self._font:
      self._font[size] = self.load_impl(self._path, size)
    return self._font[size]
  
  def load_impl(self, path, size):
    return None