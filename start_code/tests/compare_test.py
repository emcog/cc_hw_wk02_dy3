import unittest
from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_equals(self):
        self.assertEqual(" 5 == 5", compare(5, 5))



#     Write a test that will make you handle the situation when both numbers are the same
# Run the test and see check it fails (and that you've written it correctly!)
# Write the code to pass the test
# Run the code and check the tests pass (or fix any errors and run the tests again)