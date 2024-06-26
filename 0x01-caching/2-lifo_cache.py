#!/usr/bin/env python3
# 2-lifo_cache.py

""" Caching Exercises """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Caching Class with LIFO Algorithm """
    def __init__(self):
        """ Class initializer """
        super().__init__()
        self.last_key = []

    def put(self, key, item):
        """ Adds items to a finite cache using Lifo philosophy """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ Retrieves items in the cache using a key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
