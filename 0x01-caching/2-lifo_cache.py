#!/usr/bin/env pythpn3
"""class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Documentation
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put Fucntion with LIFO
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(last_key))
            self.cache_data.pop(last_key)

    def get(self, key):
        """Get Function getting item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
