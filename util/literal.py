from proto.literal_pb2 import LiteralMap
from util import cfg

class Literal:
  def __init__(self):
    self._map = LiteralMap()
    
  def load(self, path):
    cfg.load_from_file(path, self._map)

  def contains(self, key):
    return key in self._map.literal
    
  def get(self, key):
    if key in self._map.literal:
      return self._map.literal[key]
    else:
      return None