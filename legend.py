import pygame

class LegendApp:
  def __init__(self):
    self._running = False
    self._surface = None
 
  def init(self):
    self._running = True
    pygame.init()
    self._surface = pygame.display.set_mode((1200, 800))

  def on_event(self, event):
    if event.type == pygame.QUIT:
      self._running = False
      
  def on_loop(self):
    pass
    
  def on_render(self):
    pygame.display.update()
    
  def cleanup(self):
    pygame.quit()
    
  def run(self):
    self.init()
    while self._running == True:
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self.cleanup()