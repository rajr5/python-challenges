import unittest
from cache_decorator import CacheDecorator
from random import randint
from time import sleep

# Random function is a straightforward way to check wether we get the same (cached) result or not.
# This way we can avoid checking implementation details, which'll provide us with better tests.
def get_random_number(*args):
    return randint(1, 10000000)


class TestCacheDecorator(unittest.TestCase):
    def test_repeated_access_cache(self):
        cached_random_function = CacheDecorator()(get_random_number)

        results = []
        for i in range(0, 10):
            result = cached_random_function()
            results.append(result)

        number_of_unique_results = len(set(results))
        self.assertEqual(number_of_unique_results, 1)

    def test_time_based_cached(self):
        tenth_of_a_second = 1 / 600.0
        cached_random_function = CacheDecorator(ttl=tenth_of_a_second, noc=999999)(get_random_number)

        results = []
        for i in range(0, 20):
            result = cached_random_function()
            results.append(result)

        sleep(0.15)

        for i in range(0, 20):
            result = cached_random_function()
            results.append(result)

        number_of_unique_results = len(set(results))
        self.assertEqual(number_of_unique_results, 2)

    def test_different_keys(self):
        cached_random_function = CacheDecorator()(get_random_number)
        
        result1 = cached_random_function(2)
        result2 = cached_random_function(1)
        
        self.assertNotEqual(result1, result2)

    def test_custom_cache_count(self):
        cached_number_of_calls = 5
        cached_random_function = CacheDecorator(noc=cached_number_of_calls)(get_random_number)
        range_size = 100
        expected_different_results = range_size / cached_number_of_calls

        results = []
        for i in range(range_size):
            result = cached_random_function()
            results.append(result)

        number_of_unique_results = len(set(results))
        self.assertEqual(number_of_unique_results, expected_different_results)

if __name__ == '__main__':
    unittest.main()