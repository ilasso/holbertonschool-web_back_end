#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
#Cache = __import__('ex').Cache

cache = Cache()

cache.store(b"first")

print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
cache.store(b"forth")
print(cache.get(cache.store.__qualname__))
