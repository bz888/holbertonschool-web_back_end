#!/usr/bin/python3
"""LIFO caching module."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system with a storage limit."""

    def put(self, key, item):
        """Add an item and discard the most recently added item when the cache is full."""
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(reversed(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))
            
        self.cache_data[key] = item

    def get(self, key):
        """Return the cached value for key, or None when it is missing."""
        if key is None:
            return None
        return self.cache_data.get(key)
