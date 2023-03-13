import unittest

from stack import Spush, Spop

class TestStackFunctions(unittest.TestCase):

    def test_push(self):
        testStack = []
        expectedResult = [2]
        actualResult = Spush(testStack, 2)
        self.assertEqual (expectedResult, actualResult)

    def test_pop(self):
        testStack = [1,2,3]
        expectedResult = 2
        actualResult = Spop(testStack)
        self.assertEqual (expectedResult, actualResult)


if __name__ == "__main__":
    unittest.main()