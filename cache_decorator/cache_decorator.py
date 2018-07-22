from time import time

class CacheDecorator(object):
    """
    A decorator that stores the result of a function call and returns the cached version in
    subsequent calls (with the same parameters) for 'ttl' minutes, or 'noc' times ­­ whichever comes
    first.
    """
    def __init__(self, ttl = 5, noc = 10):
        self.noc = noc
        self.ttl = ttl * 60
        self.cache = {}

    def __call__(self, func, *args, **kwargs):
        def new_func(*args, **kwargs):
            cache_key = str(args) + str(kwargs)
            is_cache_missing = self.__is_cached(cache_key) == False
        
            if (is_cache_missing):
                self.__cache(cache_key, func, *args, **kwargs)

            return self.__get_from_cache(cache_key)

        return new_func


    def __clean_cache(self, cache_key):
        self.cache.pop(cache_key)

    def __is_cached(self, cache_key):
        if (cache_key not in self.cache):
            return False

        if (self.cache[cache_key]['call_count'] <= 0):
            self.__clean_cache(cache_key)
            return False

        t = time()
        cache_time = t - self.cache[cache_key]['creation_time']
        if (cache_time >= self.ttl):
            self.__clean_cache(cache_key)
            return False

        return True

    def __cache(self, cache_key, func, *args, **kwargs):
        self.cache[cache_key] = {
            'result': func(*args, **kwargs),
            'call_count': self.noc,
            'creation_time': time()
        }

    def __get_from_cache(self, cache_key):
        self.cache[cache_key]['call_count'] -= 1
        return self.cache[cache_key]['result']
