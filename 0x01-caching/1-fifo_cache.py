#!/usr/bin/env python3
""" this module houses the FIFOCache class """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ this implememts a FIFO caching algo """

    def __init__(self):
        """ initializes class instance """

        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """ adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            self.cache_queue.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.cache_queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ retrieves the items associated with key """

        if key:
            return self.cache_data.get(key)
