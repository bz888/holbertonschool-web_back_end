
#!/usr/bin/python3
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFO caching system with a storage limit."""
    
    def put(self, key, item):
        """Add an item to the cache when its key and value are not None.
		If the cache exceeds the maximum size, remove the first item added."""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first = next(iter(self.cache_data))
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

            self.cache_data[key] = item

    def get(self, key):
        """Return the cached value for key, or None when it is missing."""
        if key is not None:
            return self.cache_data.get(key)
        return None
