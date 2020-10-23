#!/usr/bin/python3
"""0-basic_cache.py:
Create a class BasicCache that inherits from BaseCaching and
is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        def put(self, key, item):
            Must assign to the dictionary self.cache_data the item value for the key
            If key or item is None, this method should not do anything.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        def get(self, key):
            Must return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

# minitest: if __name__ == "__main__":
#    b = BasicCache()
#    print(b.print_cache())
#    b.put("hola","mundo")
#    print(dir(b))
