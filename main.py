import legend
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

if __name__ == "__main__":
  app = legend.LegendApp()
  app.on_execute()