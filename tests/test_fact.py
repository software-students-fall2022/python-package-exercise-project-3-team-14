import random
from src.dailydose import fact


class Tests:

    #
    # Test functions
    #

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_get_default(self):
        """
        Verify get() function works with default params and make sure it returns an list of dict objects.
        """
        for i in range(100):
            actual = fact.get()

            assert isinstance(
                actual, list), f"Expected get() to return a list. Instead, it returned {actual}"

            assert len(
                actual) == 1, f"Expected get() to return list of length 1 by default. Instead, it returned a list of length {len(actual)}"

            assert isinstance(
                actual[0], dict), f"Expected get() to return a list of dict objects. Instead, it returned {actual[0]}"

            assert "heading" in actual[0].keys(
            ), f"Expected get() to return a list of dict objects containing 'heading' field. Instead, it returned field(s) {actual[0].keys()}"

            assert "content" in actual[0].keys(
            ), f"Expected get() to return a list of dict objects containing 'content' field by default. Instead, it returned field(s) {actual[0].keys()}"

            assert len(
                actual[0]['heading']) > 0, f"Expected 'heading' field not to be empty. Instead, it returned a string with {len(actual[0]['heading'])} characters"

            assert len(
                actual[0]['content']) > 0, f"Expected 'content' field not to be empty. Instead, it returned a string with {len(actual[0]['content'])} characters"

    def test_get_count_params(self):
        """
        Verify get() function works with `count` param.
        """

        for i in range(100):
            random_count = random.randint(1, 100)

            actual = fact.get(count=random_count)

            assert isinstance(
                actual, list), f"Expected get() to return a list. Instead, it returned {actual}"

            assert len(
                actual) == random_count, f"Expected get() to return list of length 1 by default. Instead, it returned a list of length {len(actual)}"

            random_index = random.randint(0, random_count-1)

            assert isinstance(
                actual[random_index], dict), f"Expected get() to return a list of dict objects. Instead, it returned {actual[random_index]}"

            assert "heading" in actual[random_index].keys(
            ), f"Expected get() to return a list of dict objects containing 'heading' field. Instead, it returned field(s) {actual[random_index].keys()}"

            assert "content" in actual[random_index].keys(
            ), f"Expected get() to return a list of dict objects containing 'content' field by default. Instead, it returned field(s) {actual[random_index].keys()}"

            assert len(
                actual[random_index]['heading']) > 0, f"Expected 'heading' field not to be empty. Instead, it returned a string with {len(actual[random_index]['heading'])} characters"

            assert len(
                actual[random_index]['content']) > 0, f"Expected 'content' field not to be empty. Instead, it returned a string with {len(actual[random_index]['content'])} characters"

    def test_get_include_details_params(self):
        """
        Verify get() function works with `include_details` param.
        """

        for i in range(100):
            random_include_details = random.choice([True, False])

            actual = fact.get(include_details=random_include_details)

            assert isinstance(
                actual, list), f"Expected get() to return a list. Instead, it returned {actual}"

            assert "heading" in actual[0].keys(
            ), f"Expected get() to return a list of dict objects containing 'heading' field. Instead, it returned field(s) {actual[0].keys()}"

            assert len(
                actual[0]['heading']) > 0, f"Expected 'heading' field not to be empty. Instead, it returned a string with {len(actual[0]['heading'])} characters"

            if random_include_details:
                assert "content" in actual[0].keys(
                ), f"Expected get() to return a list of dict objects containing 'content' field by default. Instead, it returned field(s) {actual[0].keys()}"

                assert len(
                    actual[0]['content']) > 0, f"Expected 'content' field not to be empty. Instead, it returned a string with {len(actual[0]['content'])} characters"
            else:
                assert "content" not in actual[0].keys(
                ), f"Expected get() to return a list of dict objects containing 'content' field by default. Instead, it returned field(s) {actual[0].keys()}"
