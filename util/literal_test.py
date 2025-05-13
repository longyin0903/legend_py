import unittest
import os
from proto.literal_pb2 import LiteralMap
from util import literal
from util import cfg

class LiteralTest(unittest.TestCase):
  def test_Load(self):
    expected = LiteralMap()
    expected.literal["key1"] = "value1"
    expected.literal["key2"] = "value2"
    cfg.save_to_file("test.dummy", expected)
    lit = literal.Literal()
    lit.load("test.dummy")
    self.assertEqual("value1", lit.get("key1"))
    self.assertEqual("value2", lit.get("key2"))
    self.assertEqual(None, lit.get("not-exist"))
    self.assertTrue(lit.contains("key1"))
    self.assertTrue(lit.contains("key2"))
    self.assertFalse(lit.contains("not-exist"))
    os.remove("test.dummy")
  
  
if __name__ == '__main__':
  unittest.main()