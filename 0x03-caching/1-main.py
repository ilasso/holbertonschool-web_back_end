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

my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("B", "Street")
my_cache.print_cache()
my_cache.put("A", "Casa")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
