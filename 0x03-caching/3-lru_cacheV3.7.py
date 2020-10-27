#!/usr/bin/python3
"""
3-lru_cache: module to create a LRUCache Class
You must use self.cache_data - dictionary from the parent class BaseCaching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache:inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        You can overload def __init__(self): but don’t forget to call
        the parent init: super().__init__()
        """
        super().__init__()
        self.lastin = enumerate(self.cache_data)

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the least recently used item (LRU algorithm)
            you must print DISCARD: with the key discarded and following by
            a new line
        """
        if key and item:
            # if key in dict shout be delete to enumerate correctly
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            self.lastin = enumerate(self.cache_data)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                w = next(self.lastin)  # firs in
                self.cache_data.pop(w[1])  # firs out
                print("DISCARD: {}".format(w[1]))
        return None

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        mark last recenty user key
        """
        if key in self.cache_data and key:
            val = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = val
            self.lastin = enumerate(self.cache_data)  # mark last used
            return self.cache_data[key]

        return None
