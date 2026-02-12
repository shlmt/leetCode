from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = dict() # key: key, value: frequence key
        self.cache = defaultdict(OrderedDict) # key: frequence key, value: OrderedDict with values
        self.min_freq = 0

    def update_usage(self, freq, key, value):
        self.cache[freq+1][key] = value
        self.counter[key] = freq+1
        del self.cache[freq][key]
        prev_freq_dict = self.cache[freq]
        if len(prev_freq_dict) == 0:
            if freq == self.min_freq:
                self.min_freq += 1
            del self.cache[freq]

    def get(self, key: int) -> int:
        freq = self.counter.get(key, -1)
        if freq == -1:
            return -1
        value = self.cache[freq][key]
        self.update_usage(freq, key, value)
        return value

    def put(self, key: int, value: int) -> None:
        freq = self.counter.get(key, -1)
        if freq != -1:
            self.update_usage(freq, key, value)
        else:
            if len(self.counter) >= self.capacity:
                k, v = self.cache[self.min_freq].popitem(last=False)
                del self.counter[k]
            self.min_freq = 1
            self.cache[1][key] = value
            self.counter[key] = 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)