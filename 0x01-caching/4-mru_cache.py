#!/usr/bin/env python3
""" this module contains the class MRUCahe """
from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
    """ this class implements the LRU cache algorithm """

    def __init__(self):
        """ initializes class instance """

        super().__init__()
        self.cache_queue = {}

    def put(self, key, item):
        """ adds a new item to the cache dict """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = min(self.cache_queue, key=self.cache.get)
                del self.cache_data[discard]
                del self.cache_queue[discard]
                print("DISCARD: {}".format(discard))
            self.cache_queue[key] = datetime.now()

    def get(self, key):
        """ retrieves item associated with key """

        if key and key in self.cache_data:
            self.cache_queue[key] = datetime.now()
            return self.cache_data.get(key)
