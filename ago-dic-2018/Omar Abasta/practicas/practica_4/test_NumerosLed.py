import unittest
from NumerosLed import NumerosLed

class TestNumerosLed(unittest.TestCase):

    def setUp(self):
        pass

    def testNumeroled1(self):
        result = NumerosLed(1)
        self.assertEqual(result,2)

    def testNumeroled8888(self):
        result = NumerosLed(8888)
        self.assertEqual(result,28)

    def testNumeroled115380(self):
        result = NumerosLed(115380)
        self.assertEqual(result,27)

    def testNumeroled2819311(self):
        result = NumerosLed(2819311)
        self.assertEqual(result,29)

    def testNumeroled23456(self):
        result = NumerosLed(23456)
        self.assertEqual(result,25)

if __name__ == '__main__':
    unittest.main()
