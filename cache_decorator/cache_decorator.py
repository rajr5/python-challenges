from time import time


class CacheDecorator(object):
    """
    A decorator that stores the result of a function call and
    returns the cached version in subsequent calls (with the same parameters)
    for 'ttl' seconds (default is 5 minutes), or
    'call_limit' times ­­(default is 10), whichever comes first.
    """

    def __init__(self, ttl_seconds=5 * 60, call_limit=10):
        self.call_limit = call_limit
        self.ttl_seconds = ttl_seconds
        self.cache = {}

    def __call__(self, func, *args, **kwargs):
        def new_func(*args, **kwargs):
            cache_key = self.__generate_key(*args, **kwargs)

            if (not self.__is_cached(cache_key)):
                self.__cache(cache_key, func, *args, **kwargs)

            return self.__get_from_cache(cache_key)

        return new_func

    def __generate_key(*args, **kwargs):
        return str(args) + str(kwargs)

    def __clean_cache(self, cache_key):
        self.cache.pop(cache_key)

    def __is_cached(self, cache_key):
        if (cache_key not in self.cache):
            return False

        if (self.cache[cache_key]['left_calls'] <= 0):
            self.__clean_cache(cache_key)
            return False

        cached_time = time() - self.cache[cache_key]['cached_time']

        if (cached_time >= self.ttl_seconds):
            self.__clean_cache(cache_key)
            return False

        return True

    def __cache(self, cache_key, func, *args, **kwargs):
        self.cache[cache_key] = {
            'result_value': func(*args, **kwargs),
            'left_calls': self.call_limit,
            'cached_time': time()
        }

    def __get_from_cache(self, cache_key):
        self.cache[cache_key]['left_calls'] -= 1
        return self.cache[cache_key]['result_value']
