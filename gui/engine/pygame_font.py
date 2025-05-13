import pygame
from gui.engine import font

class PygameFont(font.Font): 
  def load_impl(self, path, size):
    return pygame.font.Font(self._path, size)