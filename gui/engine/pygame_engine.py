import pygame

from gui.engine import engine
from gui.engine import event
from gui.engine import pygame_font

class PygameEngine(engine.Engine):
  def init(self):
    pygame.init()
  
  def cleanup(self):
    pygame.quit()
    
  def get_event(self):
    events = []
    for ev in pygame.event.get():
      if ev.type == pygame.QUIT:
        events.append(event.Event({"type": "QUIT"}))
    return events
  
  def resize(self, width, height):
    self._display = pygame.display.set_mode((width, height))

  def set_title(self, title):
    pygame.display.set_caption(title)
    
  def load_font(self, path):
    self._font = pygame_font.PygameFont()
    self._font.load(path)
  
  def get_font(self):
    return self._font
    
  def flip(self):
    pygame.display.flip()
    
  def update(self, rect):
    pygame.display.update(
        pygame.Rect(rect.left(), rect.top(), rect.width(), rect.height()))