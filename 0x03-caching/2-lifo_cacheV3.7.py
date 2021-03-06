#!/usr/bin/python3
"""
2-lifo_cache: module to create a LIFOCache Class
You must use self.cache_data - dictionary from the parent class BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache:inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        You can overload def __init__(self): but don’t forget to call
        the parent init: super().__init__()
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded and following by
            a new line
        """
        if key and item:
            # if key in dict shout be delete to enumerate correctly
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            x = enumerate(self.cache_data)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                i = 0
                while i < BaseCaching.MAX_ITEMS:
                    w = next(x)
                    i = i + 1
                self.cache_data.pop(w[1])  # firs out
                print("DISCARD: {}".format(w[1]))
        return None

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key in self.cache_data and key:
            return self.cache_data[key]
        return None
