#!/usr/bin/env python3
# 4-mru_cache.py

""" Caching Exercises """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU(Most recently Used) Caching Class """
    def __init__(self):
        """ Initializes the class instance. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache using an MRU Algorithm """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Retrieves an item from the cache using key """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
