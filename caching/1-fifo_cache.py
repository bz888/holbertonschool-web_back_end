#!/usr/bin/python3
"""FIFO caching module."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system with a storage limit."""

    def put(self, key, item):
        """Add an item and discard the oldest item when the cache is full."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Return the cached value for key, or None when it is missing."""
        if key is None:
            return None
        return self.cache_data.get(key)
