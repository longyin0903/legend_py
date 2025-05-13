from proto.game_setting_pb2 import GameSetting
from gui.engine import pygame_font
from util.literal import Literal
from util import cfg

class GameMod:
  def __init__(self, root):
    self._root = root
    self._game_setting = GameSetting()
    self._literal = Literal()

  def data_path(self, relative_path):
    return self._root + "/" + relative_path
    
  def load(self):
    # Load game setting.
    cfg.load_from_file(
        self.data_path('config/game_setting.cfg'), self._game_setting)
    self._literal.load(self.data_path("config/literal.cfg"))

  def game_setting(self):
    return self._game_setting

  def literal(self):
    return self._literal
 