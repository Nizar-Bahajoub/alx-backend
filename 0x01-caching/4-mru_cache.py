#!/usr/bin/env python3
"""class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache Documented
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put function using LRU
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get funtion
        """
        if key is None or key not in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
