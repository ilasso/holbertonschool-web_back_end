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
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                x = enumerate(self.cache_data)
                w = next(x) # firs in
                self.cache_data.pop(w[1]) # firs out
                print(f"DISCARD: {w[1]}")
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

"""mini test: if __name__ == '__main__':
    a = FIFOCache()
    print(dir(a))
    a.print_cache()
    a.put("uno","dos")
    a.put("tres","cuatro")
    a.put("cinco","seis")
    a.put("siete","ocho")
    a.print_cache()
    x=enumerate(a.cache_data)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(x)
    a.put("nueve","deiz")
    #x=enumerate(a.cache_data)
    #print(next(x))
    #print(next(x))
    #print(next(x))
    #print(next(x))
    a.print_cache()
    a.put("once","doce")
    a.print_cache()
    a.put("trece","catorce")
    a.print_cache()
"""
