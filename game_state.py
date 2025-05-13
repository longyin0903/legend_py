import proto.game_state_pb2
import spec_handler

class GameState:
  def __init__(self):
    self._state = proto.game_state_pb2.GameState()

  def new_game(self):
    pass
    
  def load(self, path):
    self_.state =  spec_handler.load_from_file(path)
     
  def save(self, path):
    spec_handler.save_to_file(path, self._state)