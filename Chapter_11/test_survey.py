import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey."""

    # setUp() method let create one object and use it in tests
    def setUp(self):
        """Create survey object and responses to use it in all tests methods."""
        question = "What is your language? "
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["spanish", "english", "polish"]

    def test_store_single_response(self):
        """Check if single response is store properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Check if single response is store properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

