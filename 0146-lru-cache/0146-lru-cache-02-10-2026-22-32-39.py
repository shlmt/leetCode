from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            self.cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        exist = self.cache.get(key, -1)
        if exist != -1:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)