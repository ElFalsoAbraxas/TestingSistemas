import unittest
from NumerosIntermedios import sumatoria

class Testsumatoria(unittest.TestCase):

    def setUP(self):
        pass

    def testSumatoria1(self):
        result=sumatoria([6,-5])
        self.assertEqual(result, 5)

    def testSumatoria2(self):
        result=sumatoria([12,15])
        self.assertEqual(result, 13)

    def testSumatoria3(self):
        result=sumatoria([12,12])
        self.assertEqual(result, 0)

    def testSumatoria4(self):
        result=sumatoria([123,321])
        self.assertEqual(result, 21756)

    def testSumatoria5(self):
        result=sumatoria([4321,1234])
        self.assertEqual(result, 4284911)

    def testSumatoria6(self):
        result=sumatoria([-19289,7853])
        self.assertEqual(result, -77593260)

if __name__ == '__main__':
    unittest.main()
