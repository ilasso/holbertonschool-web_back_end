#!/usr/bin/env python3
""" test task 0 """

Cache = __import__('exercise').Cache

cache = Cache()

a = cache.store(b"first")
print(type(a))
