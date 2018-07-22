from time import time
from cache_decorator import CacheDecorator

if __name__ == '__main__':
    @CacheDecorator()
    def fib(n):
        if n <= 1:
            return 1
        return fib(n - 1) + fib(n - 2) 

    start_time = time()
    result = fib(100)
    end_time = time()
    print("fib(100), 1st time: {0}, computation time: {1}".format(result, str(end_time - start_time)))

    start_time2 = time()
    result2 = fib(100)
    end_time2 = time()
    print("fib(100), 2nd time: {0}, computation time: {1}".format(result2, str(end_time2 - start_time2)))
