#!/usr/bin/env python3
# 1-fifo_cache.py

""" Caching Exercises """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system that discards first item and adds new """
    def __init__(self):
        """ Class Initializer """
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """ Adds finite items to the cache via FIFO philosophy """
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
                if key not in self.cache_data.keys():
                    print("DISCARD: {}".format(self._keys[0]))
                    self.cache_data.pop(self._keys[0])
                    self._keys.pop(0)

            self.cache_data[key] = item
            if key not in self._keys:
                self._keys.append(key)

    def get(self, key):
        """ Retrieves items in cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
