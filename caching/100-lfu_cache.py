#!/usr/bin/python3
"""LFU caching module."""

from base_caching import BaseCaching


class Node:
    """A cache entry stored in a frequency list."""

    def __init__(self, key, value):
        """Initialize a cache entry with a frequency of one."""
        self.key = key
        self.value = value
        self.count = 1
        self.prev = None
        self.next = None


class LFUCache(BaseCaching):
    """Least-frequently-used caching system with an LRU tie-breaker."""

    def __init__(self):
        """Initialize the cache and frequency tracking dictionaries."""
        super().__init__()
        self.nodes = {}
        self.freq_map = {}
        self.min_freq = 0

    def put(self, key, item):
        """Add or update an item and increase its usage frequency."""
        if key is None or item is None:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = item
            self.cache_data[key] = item
            self._update_frequency(node)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            head, tail = self.freq_map[self.min_freq]
            discarded = tail.prev
            self._remove(discarded)
            del self.nodes[discarded.key]
            del self.cache_data[discarded.key]
            if head.next is tail:
                del self.freq_map[self.min_freq]
            print("DISCARD: {}".format(discarded.key))

        node = Node(key, item)
        self.nodes[key] = node
        self.cache_data[key] = item
        self.min_freq = 1
        self._add(node, 1)

    def get(self, key):
        """Return an item and increase its usage frequency."""
        if key is None or key not in self.nodes:
            return None

        node = self.nodes[key]
        self._update_frequency(node)
        return self.cache_data[key]

    def _add(self, node, frequency):
        """Add a node as most recent in a frequency list."""
        if frequency not in self.freq_map:
            head = Node(None, None)
            tail = Node(None, None)
            head.next = tail
            tail.prev = head
            self.freq_map[frequency] = (head, tail)

        head, _ = self.freq_map[frequency]
        node.prev = head
        node.next = head.next
        head.next.prev = node
        head.next = node

    def _remove(self, node):
        """Remove a node from its current frequency list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _update_frequency(self, node):
        """Move a node into the next frequency list."""
        old_frequency = node.count
        head, tail = self.freq_map[old_frequency]
        self._remove(node)

        if head.next is tail:
            del self.freq_map[old_frequency]
            if self.min_freq == old_frequency:
                self.min_freq += 1

        node.count += 1
        self._add(node, node.count)
