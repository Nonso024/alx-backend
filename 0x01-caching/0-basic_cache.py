#!/usr/bin/env python3
""" This module contains the BasicCache class """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ This implements a basic caching system """

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves item associated with give key """

        if key:
            return self.cache_data.get(key)
