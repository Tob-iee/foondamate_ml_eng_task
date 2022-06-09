import unittest
import email_classifier


class test_classifier(unittest.TestCase):
    # test the if the email has been shared or not
    def test_case_1(self):
        #capture the results of function
        result = email_classifier.classifier("Can I share your email")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

    def test_case_2(self):
        #capture the results of function
        result = email_classifier.classifier("I will share your email")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)


    def test_case_3(self):
        #capture the results of function
        result = email_classifier.classifier("I shall share your email")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)


    def test_case_4(self):
        #capture the results of function
        result = email_classifier.classifier("I've shared your email")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)

    def test_case_5(self):
        #capture the results of function
        result = email_classifier.classifier("May I share your email")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

    def test_case_6(self):
        #capture the results of function
        result = email_classifier.classifier("Should I share your email")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

    def test_case_7(self):
        #capture the results of function
        result = email_classifier.classifier("I already shared the email")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)

    def test_case_8(self):
        #capture the results of function
        result = email_classifier.classifier("I've just shared your email")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)

    def test_case_9(self):
        #capture the results of function
        result = email_classifier.classifier("Am I allowed to share your email")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

    def test_case_10(self):
        #capture the results of function
        result = email_classifier.classifier("Am I able to share your email")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

    def test_case_11(self):
        #capture the results of function
        result = email_classifier.classifier("I am able to share your email")
        # check for expected output
        expected = "Student has shared"
        self.assertEqual(expected, result)

    def test_case_12(self):
        #capture the results of function
        result = email_classifier.classifier("Will you help my friends if I share your email with them?")
        # check for expected output
        expected = "Student wants to know if can share"
        self.assertEqual(expected, result)

# Run the Tests
if __name__ == "__main__":
    unittest.main()