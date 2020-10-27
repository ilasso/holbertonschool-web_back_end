#!/home/holberton/opt/python-3.4.3/bin/python3
""" 2-main
[Expected]
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
LIFOCache = __import__('2-lifo_cache').LIFOCache


"""my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
"""

from base_caching import BaseCaching
BaseCaching.MAX_ITEMS = 1
LIFOCache.MAX_ITEMS = 1
my_cache = LIFOCache()
my_cache.MAX_ITEMS = 1

my_cache.put("key-0", "value-0")
my_cache.print_cache()
my_cache.put("key-1", "value-1")
my_cache.print_cache()
my_cache.put("key-2", "value-2")
my_cache.print_cache()
my_cache.put("key-3", "value-3")
my_cache.print_cache()
my_cache.put("key-4", "value-4")
my_cache.print_cache()
