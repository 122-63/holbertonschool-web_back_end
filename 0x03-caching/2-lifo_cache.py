#!/usr/bin/python3
"""
BaseCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """

    def __init__(self):
        """ Init """
        super().__init__()

    def put(self, key, item):
        """
            modify cache data
            Args:
                key: of the dict
                item: value of the key
        """
        if key or item is not None:
            value_cache = self.get(key)
            # Make a new
            if value_cache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())
                    lenlast = len(keydel) - 1
                    del self.cache_data[keydel[lenlast]]
                    print("DISCARD: {}".format(keydel[lenlast]))
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
            modify cache data
            Args:
                key: of the dict
            Return:
                value of the key
        """

        value_cache = self.cache_data.get(key)
        return value_cache
