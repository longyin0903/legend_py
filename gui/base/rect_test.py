import unittest
from gui.base import rect


class PointTest(unittest.TestCase):
  def test_Constructor(self):
    p = rect.Point(3, 4)
    self.assertEqual(3, p.x())
    self.assertEqual(4, p.y())
    
  def test_Equal(self):
    p = rect.Point(3, 4)
    self.assertEqual(p, rect.Point(3, 4))
    self.assertNotEqual(p, rect.Point(3, 5))
    self.assertNotEqual(p, rect.Point(2, 4))
    self.assertNotEqual(p, rect.Point(2, 5))
    
class RectSizeTest(unittest.TestCase):
  def test_Constructor(self):
    s = rect.Rect.Size(3, 4)
    self.assertEqual(3, s.width())
    self.assertEqual(4, s.height())

  def test_Equal(self):
    p = rect.Rect.Size(3, 4)
    self.assertEqual(p, rect.Rect.Size(3, 4))
    self.assertNotEqual(p, rect.Rect.Size(3, 5))
    self.assertNotEqual(p, rect.Rect.Size(2, 4))
    self.assertNotEqual(p, rect.Rect.Size(2, 5))

class RectTest(unittest.TestCase):
  def test_Constructor(self):
    r = rect.Rect(3, 4, 5, 6)
    self.assertEqual(3, r.left())
    self.assertEqual(4, r.top())    
    self.assertEqual(5, r.width())
    self.assertEqual(6, r.height())  

  def test_Position(self):
    r = rect.Rect(3, 4, 5, 6)
    self.assertEqual(rect.Point(3, 4), r.position())

  def test_Size(self):
    r = rect.Rect(3, 4, 5, 6)
    self.assertEqual(rect.Rect.Size(5, 6), r.size())

  def test_Getter(self):
    r = rect.Rect(3, 4, 5, 6)
    self.assertEqual(3, r.left())
    self.assertEqual(4, r.top())
    self.assertEqual(5, r.width())
    self.assertEqual(6, r.height())
    self.assertEqual(8, r.right())
    self.assertEqual(10, r.bottom())

  def test_MoveTo(self):
    r = rect.Rect(3, 4, 5, 6)
    self.assertEqual(3, r.left())
    self.assertEqual(4, r.top())
    self.assertEqual(5, r.width())
    self.assertEqual(6, r.height())
    r.moveto(23, 41)
    self.assertEqual(23, r.left())
    self.assertEqual(41, r.top())
    self.assertEqual(5, r.width())
    self.assertEqual(6, r.height())

  def test_Resize(self):
    r = rect.Rect(3, 4, 5, 6)
    self.assertEqual(3, r.left())
    self.assertEqual(4, r.top())
    self.assertEqual(5, r.width())
    self.assertEqual(6, r.height())
    r.resize(23, 41)
    self.assertEqual(3, r.left())
    self.assertEqual(4, r.top())
    self.assertEqual(23, r.width())
    self.assertEqual(41, r.height())    
    
if __name__ == '__main__':
  unittest.main()