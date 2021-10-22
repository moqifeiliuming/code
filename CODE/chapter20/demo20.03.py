import unittest,demo20_02
class TestCase(unittest.TestCase):
    def testSquare(self):
        for x in range(-20,20):
            result = demo20_02.square(x)
            self.assertEqual(result, x * x, '%d的二次方失败' % x)
    def testAdd(self):
        for x in range(-20,20):
            for y in range(-10,10):
                result = demo20_02.add(x,y)
                self.assertEqual(result, x + y, '%d + %d失败' % (x,y))

if __name__ == '__main__':
    unittest.main()     