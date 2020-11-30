#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

a = cache.store(b"first")
print(a)
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
cache.store(b"forth")
print(cache.get(cache.store.__qualname__))
