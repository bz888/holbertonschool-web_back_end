#!/usr/bin/python3
"""MRU caching module."""

from base_caching import BaseCaching


class Node:
    """A node in the doubly linked recency list."""

    def __init__(self, key, value):
        """Initialize a node with a cache key and value."""
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class MRUCache(BaseCaching):
    """Most-recently-used caching system with a storage limit."""

    def __init__(self):
        """Initialize the cache and its recency list."""
        super().__init__()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    def put(self, key, item):
        """Add or update an item and mark it as most recently used."""
        if key is None or item is None:
            return

        if key in self.nodes:
            node = self.nodes[key]
            self._remove(node)
            node.value = item
        else:
            node = Node(key, item)
            self.nodes[key] = node

        self.cache_data[key] = item
        self._add(node)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_node = self.head.next
            self._remove(mru_node)
            del self.nodes[mru_node.key]
            del self.cache_data[mru_node.key]
            print("DISCARD: {}".format(mru_node.key))

    def get(self, key):
        """Return a value and mark its key as most recently used."""
        if key is None or key not in self.cache_data:
            return None

        node = self.nodes[key]
        self._remove(node)
        self._add(node)
        return self.cache_data[key]

    def _add(self, node):
        """Insert a node immediately after the dummy head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Remove a node from the recency list."""
        node.prev.next = node.next
        node.next.prev = node.prev
