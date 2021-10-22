import unittest,solution20_1
import numpy

class TestCase(unittest.TestCase):
    def testSquare(self):
        for x in range(0,10):
            result = solution20_1.factorial(x)
            self.assertEqual(result, numpy.math.factorial(x), '%d的阶乘失败' % x)

if __name__ == '__main__':
    unittest.main()     