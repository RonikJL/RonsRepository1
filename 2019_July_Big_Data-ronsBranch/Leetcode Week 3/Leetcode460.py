import collections


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.k = capacity
        self.cacheFreq = collections.defaultdict(collections.OrderedDict)
        self.cacheKey = {}
        self.leastFreq = 1

    def _evict(self):
        key, _ = self.cacheFreq[self.leastFreq].popitem(last=False)
        del self.cacheKey[key]

    def _update(self, key, new_v=None):
        freq, v = self.cacheKey[key]['freq'], self.cacheKey[key]['value']
        del self.cacheFreq[freq][key]
        if not self.cacheFreq[self.leastFreq]:
            self.leastFreq += 1

        self.cacheKey[key] = {'freq': freq + 1, 'value': new_v or v}
        self.cacheFreq[freq + 1][key] = new_v or v

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cacheKey:
            return -1
        self._update(key)
        return self.cacheKey[key]['value']

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cacheKey:
            self._update(key, value)
            return
        self.cacheKey[key] = {'freq': 1, 'value': value}
        self.cacheFreq[1][key] = value
        if len(self.cacheKey) > self.k:
            self._evict()
        self.leastFreq = 1
