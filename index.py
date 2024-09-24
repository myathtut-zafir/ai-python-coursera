import unittest
from add import add

class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        result = add(2,2)
        self.assertEqual(result,4)
unittest.main()
