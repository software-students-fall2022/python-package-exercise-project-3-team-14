from english_words import english_words_set
import random
import string
from src.dailydose import hang


class Tests:

    #Test functions

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_hangman_length(monkeypatch):
        """
        Test the length of the word returned
        The word should have length in between 4 and 10
        """
        monkeypatch.setattr('builtins.input', lambda _: random.choice(string.ascii_letters))
        for i in range(-1, 12):
            actual = len(hang.hangman(i))
            assert actual >= 4 or actual <= 10, f"Expect the length of word to be between 4 and 10"

    def test_hangman_word(monkeypatch):
        """
        Test if the word is in the set of english word
        """
        monkeypatch.setattr('builtins.input', lambda _: random.choice(string.ascii_letters))
        for i in range(-1, 12):
            actual = hang.hangman(i)
            assert actual in english_words_set, f"Expect word to be in the set of English word"

    def test_hangman_input(monkeypatch):
        """
        Test if function works properly with abnormal input
        """
        monkeypatch.setattr('builtins.input', lambda _: random.choice(string.ascii_letters))
        actual = hang.hangman("a")
        assert actual == "code 1", f"Expect the function to return code 1 for abnormal input"
        actual1 = hang.hangman(" ")
        assert actual1 == "code 1", f"Expect the function to return code 1 for abnormal input"
        actual2 = hang.hangman("\n")
        assert actual2 == "code 1", f"Expect the function to return code 1 for abnormal input"
        actual3 = hang.hangman(4.1)
        assert actual3 == "code 1", f"Expect the function to return code 1 for abnormal input"