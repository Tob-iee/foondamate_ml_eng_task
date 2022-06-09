import unittest
import email_classifier



class test_classifier(unittest.TestCase):
    # test the if the email has been shared or not
    def test_for_share(self):
        #capture the results of function
        result = email_classifier.classifier("Will you help my friends if I share your email with them?")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)

    def test_for_not_share(self):
        #capture the results of function
        result = email_classifier.classifier("I am able to share your email")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

# Run the Tests
if __name__ == "__main__":
    unittest.main()