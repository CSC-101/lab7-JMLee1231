import unittest
from convert import str_to_float


class TestStrToFloat(unittest.TestCase):

    def test_valid_float_conversion(self):
        result = str_to_float("3.14")
        self.assertEqual(result, 3.14)
        result = str_to_float("42")
        self.assertEqual(result, 42.0)

    def test_invalid_conversion(self):

        result = str_to_float("abc")
        self.assertIsNone(result)


# Run the tests
if __name__ == '__main__':
    unittest.main()

