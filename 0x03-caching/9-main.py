#!/usr/bin/python3
"""
Test
BaseCaching.MAX_ITEMS = 1 add 5 items
got:

key-0: value-0
DISCARD: key-1
Current cache:
key-0: value-0
DISCARD: key-2
Current cache:
key-0: value-0
DISCARD: key-3
Current cache:
key-0: value-0
DISCARD: key-4
Current cache:
key-0: value-0

expected:

Current cache:
key-0: value-0
DISCARD: key-0
Current cache:
key-1: value-1
DISCARD: key-1
Current cache:
key-2: value-2
DISCARD: key-2
Current cache:
key-3: value-3
DISCARD: key-3
Current cache:
key-4: value-4
"""
import sys

try:
    FIFOCache = __import__('1-fifo_cache').FIFOCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 1
    FIFOCache.MAX_ITEMS = 1
    my_cache = FIFOCache()
    my_cache.MAX_ITEMS = 1

    for i in range(5):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        my_cache.put(key, value)
        my_cache.print_cache()

except:
    print(sys.exc_info()[1])
