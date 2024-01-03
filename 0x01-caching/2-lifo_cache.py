#!/usr/bin/env python3
""" this module houses the class LIFOCache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ this class implements the LIFO caching algo """

    def __init__(self):
        """ initializes the class instance """

        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.cache_queue.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_queue.append(key)

    def get(self, key):
        """ retrieves the item associated with key """

        if key:
            return self.cache_data.get(key)
