from src.dailydose import news

class TestNews:

    subjects = ["culture", "policy-and-politics", "science-and-health", "world", "technology", "energy-and-environment", "business-and-finance"]
    titulars = ["CULTURE", "POLITICS AND POLICY", "SCIENCE AND HEALTH", "WORLD", "TECHNOLOGY", "ENERGY AND ENVIRONMENT", "BUSINESS AND FINANCE"]

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_validate_url(self):
        """
        Test the validate_url function to ensure webpages are being accessed correctly. 
        """
        expected = 200
        for subject in self.subjects:
            go = news.validate_url(subject)
            actual = go.status_code
            assert actual == expected, f"Expected {expected} to be equal to {actual}. This is the status code of the webpage for {subject} news."
        
        dummy = news.validate_url("invalid")
        assert dummy.status_code >= 400, f"Invalid subject passed as param. Expect a 400+ status code, received {dummy.status_code}."

    def test_get_list(self):
        """
        Test the get_list function to make sure a nonempty list of strings is returned.
        """

        for subject in self.subjects:
            go = news.validate_url(subject)
            actual = news.get_list(go)
            assert len(actual) != 0, f"Headlines found for {subject}: {len(actual)}"
            assert type(actual[0]) == str, f"Headlines are expected to be of type string. Received {type(actual[0])}."

    def test_get_headlines(self):
        """
        Test the get_headlines function. Ensure valid inputs are processed correctly and invalid webpages are handled.
        """
        for subject in self.subjects:
            actual = news.get_headlines(subject, "SUBJECT")
            assert type(actual) == list, f"Expected a return type of list. Received {type(actual)}."

        expected2 = False
        actual2 = news.get_headlines("invalid", "INVALID")
        assert actual2 == expected2, f"Test for invalid subject. Expected a return value of {expected}. Received {actual}."


          
