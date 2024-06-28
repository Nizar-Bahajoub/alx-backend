#!/usr/bin/env python3
"""class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache Documented
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put function using LRU
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        last_key = key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, lru_value = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """Get funtion
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
