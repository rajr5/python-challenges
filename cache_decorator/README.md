# Cache decorator

The solution consists of:

- `main.py` - a runnable example
- `cache_decorator.py` - the solution
- `cache_decorator.test.py` - unit tests for the solution

## The problem

Write a decorator that stores the result of a function call and returns the cached version in
subsequent calls (with the same parameters) for 5 minutes, or ten times whichever comes
first.

## Approach to the problem

The problem is implemented in the `CacheDecorator` class. By default the solution caches the result for 5 minutes or for 10 subsequent calls, the cached length can be changed via `ttl_seconds` and `call_limit` decorator parameteres.

Python 3.x provides the `lru_cache` decorator that could've been used for the solution which would greatly simplify our code but it since it solves most of the problem by itself it could be considered cheating.

## Solution efficiency

Since the solution varies greatly deppending on the kind of functions and their parameters we're caching I'll try giving an estimate.

### Time complexity

If we're looking at the worst time it depends on the function/method we're trying to cache, but every cached call will have a time complexity of O(1) which is great if we're using the cache decorator for a function whose parameters aren't being changed very often.

Time complexity evaluation based on: https://wiki.python.org/moin/TimeComplexity

### Space complexity

The space complexity depends on the functions we cache, number of functions, their parameters and return values.


## Unit tests

We could test the solution in a couple of ways, first can use the `CacheDecorator` internals to check wether the timer and counters are being updated properly but that would result in brittle tests which would need to be updated each time the decorator implementation changes, so I've implemented the tests based on a random number generator. The logic is that if we call the random number generator function a few times and get all the same values it means they're properly cached (unless python has a very poor standard number generator), if we get different solutions, it means the cache has been invalidated. I believe we could also use time_ns() in the same way, 