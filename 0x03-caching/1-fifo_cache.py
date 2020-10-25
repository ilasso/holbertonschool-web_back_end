#!/usr/bin/python3
"""
1-fifo.cache: module to create a FIFOCache Class
You must use self.cache_data - dictionary from the parent class BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache:inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        You can overload def __init__(self): but don’t forget to call
        the parent init: super().__init__()
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value for
        the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the first item put in cache (FIFO algorithm)
            you must print DISCARD: with the key discarded and following
            by a new line
        """

        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            x = enumerate(self.cache_data)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                w = next(x)  # firs in
                del self.cache_data[w[1]]  # firs out
                print("DISCARD: {}".format(w[1]))

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data and key:
            return self.cache_data[key]
        return None
