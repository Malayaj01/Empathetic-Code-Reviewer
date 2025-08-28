import unittest
from src.reviewer import transform_comment

class TestReviewer(unittest.TestCase):

    def test_transform_harsh_comment(self):
        harsh_comment = "This code is terrible and poorly written."
        expected_feedback = "I see that you might be feeling frustrated with this code. Let's work together to improve it!"
        self.assertEqual(transform_comment(harsh_comment), expected_feedback)

    def test_transform_mixed_comment(self):
        mixed_comment = "The logic is good, but the implementation is messy."
        expected_feedback = "It's great that you recognize the good logic! Let's focus on tidying up the implementation."
        self.assertEqual(transform_comment(mixed_comment), expected_feedback)

    def test_transform_positive_comment(self):
        positive_comment = "This is a great piece of code!"
        expected_feedback = "Thank you for your positive feedback! It's encouraging to hear that."
        self.assertEqual(transform_comment(positive_comment), expected_feedback)

    def test_transform_empty_comment(self):
        empty_comment = ""
        expected_feedback = "It seems like there might be some thoughts missing. Could you elaborate?"
        self.assertEqual(transform_comment(empty_comment), expected_feedback)

if __name__ == '__main__':
    unittest.main()