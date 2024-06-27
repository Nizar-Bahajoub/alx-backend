#!/usr/bin/env python3
"""class BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]
