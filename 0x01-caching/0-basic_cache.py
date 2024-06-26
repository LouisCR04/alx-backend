#!/usr/bin/env python3
# 0-basic_cache.py

""" Caching Exercises """

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Put & Get caching system"""
    def put(self, key, item):
        """ Adds items to the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves cached items using a key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
