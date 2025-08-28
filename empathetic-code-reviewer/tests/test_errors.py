import unittest
from src.errors import CustomError

class TestErrorHandling(unittest.TestCase):

    def test_custom_error_raised(self):
        with self.assertRaises(CustomError):
            raise CustomError("This is a custom error message.")

    def test_another_error_handling(self):
        # Assuming there's another custom error to test
        with self.assertRaises(CustomError):
            raise CustomError("Another error occurred.")

if __name__ == '__main__':
    unittest.main()