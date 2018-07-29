import unittest
from cache_decorator import CacheDecorator
from random import randint
from time import sleep


def get_random_number(*args):
    """
    Random function is a straightforward way to check wether we
    get the same (cached) result or not. This way we can avoid
    checking implementation details, which'll provide us with better tests.
    We provided *args as a param so we can more easily test
    for different inputs to the function.
    """
    return randint(1, 10000000)


class TestCacheDecorator(unittest.TestCase):
    def test_repeated_access_cache(self):
        cached_random_function = CacheDecorator()(get_random_number)
        results = []

        for _ in range(10):
            result = cached_random_function()
            results.append(result)

        number_of_unique_results = len(set(results))
        self.assertEqual(number_of_unique_results, 1)

    def test_time_based_cache(self):
        cached_random_function = CacheDecorator(
            ttl_seconds=0.1,
            call_limit=999999
        )(get_random_number)
        results = []

        for _ in range(10):
            result = cached_random_function()
            results.append(result)

        sleep(0.11)

        for _ in range(10):
            result = cached_random_function()
            results.append(result)

        number_of_unique_results = len(set(results))

        self.assertEqual(number_of_unique_results, 2)

    def test_different_keys_not_being_cached(self):
        cached_random_function = CacheDecorator()(get_random_number)
        range_size = 10
        results = []

        for i in range(range_size):
            result = cached_random_function(i)
            results.append(result)

        number_of_unique_results = len(set(results))

        self.assertEqual(number_of_unique_results, range_size)

    def test_custom_cache_count(self):
        cached_number_of_calls = 5
        cached_random_function = CacheDecorator(
            call_limit=cached_number_of_calls
        )(get_random_number)
        range_size = 50
        expected_different_results = range_size / cached_number_of_calls
        results = []

        for _ in range(range_size):
            result = cached_random_function()
            results.append(result)

        number_of_unique_results = len(set(results))

        self.assertEqual(number_of_unique_results, expected_different_results)


if __name__ == '__main__':
    unittest.main()
