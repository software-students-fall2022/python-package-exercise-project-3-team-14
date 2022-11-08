from _pytest.monkeypatch import MonkeyPatch
from english_words import english_words_lower_alpha_set
import string
from src.dailydose import hang


class Tests:

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_hangman_length(self):
        """
        Test the length of the word returned
        The word should have length in between 4 and 10
        """
        self.monkeypatch = MonkeyPatch()
        iter_list = []
        for i in range(13):
            iter_list.append(iter(list(string.ascii_lowercase)))
        for i in range(-1, 12):
            j = i+1
            self.monkeypatch.setattr('builtins.input', lambda _: next(iter_list[j]))
            actual = len(hang.hangman(i))
            assert actual >= 4 or actual <= 10, f"Expect the length of word to be between 4 and 10"

    def test_hangman_word(self):
        """
        Test if the word is in the set of english word
        """
        self.monkeypatch = MonkeyPatch()
        iter_list = []
        for i in range(13):
            iter_list.append(iter(list(string.ascii_lowercase)))
        for i in range(-1, 12):
            j = i+1
            self.monkeypatch.setattr('builtins.input', lambda _: next(iter_list[j]))
            actual = hang.hangman(i)
            assert actual in english_words_lower_alpha_set, f"Expect word to be in the set of English word"

    def test_hangman_input(self):
        """
        Test if function works properly with abnormal input
        """
        self.monkeypatch = MonkeyPatch()
        inputs = iter(list(string.ascii_lowercase)*5)
        self.monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual = hang.hangman("a")
        assert actual == "code 1", f"Expect the function to return code 1 for abnormal input"
        self.monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual1 = hang.hangman(" ")
        assert actual1 == "code 1", f"Expect the function to return code 1 for abnormal input"
        self.monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual2 = hang.hangman("\n")
        assert actual2 == "code 1", f"Expect the function to return code 1 for abnormal input"
        self.monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual3 = hang.hangman(4.1)
        assert actual3 == "code 1", f"Expect the function to return code 1 for abnormal input"
