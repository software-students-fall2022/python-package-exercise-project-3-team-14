# import news.py

import news

#  different unit tests for news.py

# first test: sanity check
# second test: check if list is returned 
# third test: check if list is not empty
# fourth test: check if list contains strings
# fifth test: check if list contains only single word or unwanted text

class TestNews:

    def test_one(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_two(self):
        """
        Test if the function returns a list
        """
        expected = list
        actual = type(news.get_headlines())
        assert actual == expected, "Expected list to be returned!"

    def test_three(self):
        """
        Test if the function returns a list of length greater than 0
        """
        expected = True
        actual = len(news.get_headlines()) > 0
        assert actual == expected, "Expected list to be non-empty!"

    def test_four(self):
        """
        Test if the function returns a list of strings
        """
        expected = str
        actual = type(news.get_headlines()[0])
        assert actual == expected, "Expected list to contain strings!"

    def test_five(self):
        """
        Test if the function returns a list of strings of length greater than 1 and not unwanted
        """
        expected = True
        actual = len(news.get_headlines()[0].split()) > 1 and news.get_headlines()[0] not in news.unwanted
        assert actual == expected, "Expected list to contain long enough titles and not unwanted!"
        
