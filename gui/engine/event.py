class Event:
  def __init__(self, dict):
    self._dict = dict

  def _lookup_(self, type):
    if type in self._dict:
      return self._dict[type]
    raise AttributeError("event." + type + " not found")
    
  def type(self):
    return self._lookup_("type")
    
  def x(self):
    return self._lookup_("x")
    