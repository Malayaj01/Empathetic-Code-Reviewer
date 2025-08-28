import unittest
from unittest.mock import patch
from src.cli import main

class TestCLI(unittest.TestCase):

    @patch('src.cli.sys.argv', new=['cli.py', '--input', 'test_input.json'])
    def test_input_argument(self):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    @patch('src.cli.sys.argv', new=['cli.py', '--help'])
    def test_help_argument(self):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    @patch('src.cli.sys.argv', new=['cli.py', '--input', 'invalid_input.json'])
    def test_invalid_input_file(self):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertNotEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()