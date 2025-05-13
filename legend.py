from gui.engine import pygame_engine
from gui.engine import event

from game_mod import GameMod

class LegendApp:
  def __init__(self):
    self._running = True
    self._engine = pygame_engine.PygameEngine()
    
  def on_init(self):
    self._game_mod = GameMod("reko3")
    self._game_mod.load()
    self._engine.init()
    self._engine.resize(self._game_mod.game_setting().width,
                        self._game_mod.game_setting().height)
    self._engine.load_font(
        self._game_mod.data_path(self._game_mod.game_setting().font_path))
    if self._game_mod.literal().contains("GAME_TITLE"):
      self._engine.set_title(self._game_mod.literal().get("GAME_TITLE"))

  def on_event(self, event):
    if event.type() == "QUIT":
      self._running = False

  def on_loop(self):
    pass
  
  def on_render(self):
    pass
   	
  def on_execute(self):
    self.on_init()
    while self._running:
      for event in self._engine.get_event():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self._engine.cleanup()