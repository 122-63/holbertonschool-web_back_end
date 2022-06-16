#!/usr/bin/python3
"""
FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        """ Init"""
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def _pop(self):
        """ FIFO algorithm, remove element """
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]

    def _push(self, key, item):
        """ FIFO algorithm, add element """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key
    
    def put(self, key, item):
        """
            modify cache data
            Args:
                key: of the dict
                item: value of the key
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """
            modify cache data
            Args:
                key: of the dict
            Return:
                value of the key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
