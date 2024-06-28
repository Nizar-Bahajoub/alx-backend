#!/usr/bin/env python3
"""class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCche Documentation
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put Function adding items for a specific key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            disc_item = next(iter(self.cache_data))
            print("DISCARD: {}".format(disc_item))
            self.cache_data.pop(disc_item)

    def get(self, key):
        """Get Function getting items of a specific key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
