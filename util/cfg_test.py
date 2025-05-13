import os
import unittest
from util import cfg

from proto.game_setting_pb2 import GameSetting

class CfgTest(unittest.TestCase):
  def test_LoadFromString(self):
    expected = GameSetting()
    expected.width = 1024
    expected.height = 815
    expected.font_path = "path/foo"
    setting = GameSetting()
    cfg.load_from_string(
        "width: 1024 height: 815 font_path: 'path/foo'", setting)
    self.assertEqual(setting, expected)

  def test_LoadFromFile(self):
    f = open("cfg_test.dummy", "w", encoding="utf-8")
    f.write( "width: 1024 height: 815 font_path: 'path/foo'")
    f.close()
    expected = GameSetting()
    expected.width = 1024
    expected.height = 815
    expected.font_path = "path/foo"
    setting = GameSetting()
    cfg.load_from_file("cfg_test.dummy", setting)
    self.assertEqual(setting, expected)
    os.remove("cfg_test.dummy")

  def test_SaveToFile(self):
    expected = GameSetting()
    expected.width = 1024
    expected.height = 815
    expected.font_path = "path/foo"
    cfg.save_to_file("cfg_test.dummy", expected)
    setting = GameSetting()
    cfg.load_from_file("cfg_test.dummy", setting)
    self.assertEqual(setting, expected)
    os.remove("cfg_test.dummy")
    
if __name__ == '__main__':
  unittest.main()