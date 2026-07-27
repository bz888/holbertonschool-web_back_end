#!/usr/bin/python3
"""LIFO caching module."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system with a storage limit."""

    def put(self, key, item):
        """Add an item and discard the newest item when the cache is full."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[key]
            print("DISCARD: {}".format(key))

    def get(self, key):
        """Return the cached value for key, or None when it is missing."""
        if key is None:
            return None
        return self.cache_data.get(key)
