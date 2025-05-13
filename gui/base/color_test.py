import unittest
from gui.base import color


class PointTest(unittest.TestCase):
  def test_Constructor(self):
    c = color.Color(3, 4, 5, 6)
    self.assertEqual(3, c.red())
    self.assertEqual(4, c.green())
    self.assertEqual(5, c.blue())
    self.assertEqual(6, c.alpha())
    c = color.Color(3, 4, 5)
    self.assertEqual(3, c.red())
    self.assertEqual(4, c.green())
    self.assertEqual(5, c.blue())
    self.assertEqual(255, c.alpha())

  def test_Equal(self):
    c = color.Color(3, 4, 5, 6)
    self.assertEqual(c, color.Color(3, 4, 5, 6))
    self.assertNotEqual(c, color.Color(2, 4, 5, 6))
    self.assertNotEqual(c, color.Color(3, 1, 5, 6))
    self.assertNotEqual(c, color.Color(3, 4, 15, 6))
    self.assertNotEqual(c, color.Color(3, 4, 5, 8))

  def test_FromInt(self):
    c = color.Color.from_int(0x03040506)
    self.assertEqual(c, color.Color(3, 4, 5, 6))
    c = color.Color.from_int(0x83040506)
    self.assertEqual(c, color.Color(0x83, 4, 5, 6))

  def test_ToInt(self):
    c = color.Color(3, 4, 5, 6)
    self.assertEqual(0x03040506, c.to_int())
    c = color.Color(0x83, 4, 5, 6)
    self.assertEqual(0x83040506, c.to_int())
    
if __name__ == '__main__':
  unittest.main()