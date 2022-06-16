#!/usr/bin/python3
"""
Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that inherits from BaseCaching"""

    def put(self, key, item):
        """
        * Must assign to the dictionary self.cache_data
          the item value for the key key.
        * If key or item is None, this method should not do anything.
        """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        * Must return the value in self.cache_data linked to key.
        * If key is None or if the key doesn’t exist in self.cache_data,
          return None.
        """

        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
