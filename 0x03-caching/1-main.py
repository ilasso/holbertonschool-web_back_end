#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
"""my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print("insert E")
my_cache.put("E", "Battery")
my_cache.print_cache()
print("Update C")
my_cache.put("C", "Street")
my_cache.print_cache()
print("Insert F")
my_cache.put("F", "Mission")
my_cache.print_cache()
print("Insert G")
my_cache.put("G", "Mission 2")
my_cache.print_cache()"""

"""my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("B", "Street")
my_cache.print_cache()
my_cache.put("A", "Casa")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()"""

from base_caching import BaseCaching
BaseCaching.MAX_ITEMS = 1
FIFOCache.MAX_ITEMS = 1
my_cache = FIFOCache()
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
