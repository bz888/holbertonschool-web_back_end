#!/usr/bin/python3
"""Basic caching system without a storage limit."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Store and retrieve items without enforcing a cache size limit."""

    def put(self, key, item):
        """Add an item to the cache when its key and value are not None."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the cached value for key, or None when it is missing."""
        if key is not None:
            return self.cache_data.get(key)
        return None
