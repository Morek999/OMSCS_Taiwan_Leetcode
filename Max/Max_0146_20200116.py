""" 
146. LRU Cache
https:#leetcode.com/problems/lru-cache/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.cap:
            self.popitem(last=False)

""" 
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.collect = []

    def get(self, key: int) -> int:
        self.collect = dict(self.collect)
        tmp = self.collect.pop(key, -1)
        self.collect = list(self.collect.items())
        if tmp != -1:
            self.collect.append((key, tmp))
        print(tmp)
        return tmp

    def put(self, key: int, value: int) -> None:
        if len(self.collect) >= self.cap:
            if key in dict(self.collect):
                tmp = dict(self.collect)
                tmp.pop(key)
                self.collect = list(tmp.items())
            else:
                self.collect.pop(0)
        self.collect.append((key, value))
 """
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)        # returns 1
cache.put(3, 3)     # evicts key 2
cache.get(2)        # returns -1 (not found)
cache.put(4, 4)     # evicts key 1
cache.get(1)        # returns -1 (not found)
cache.get(3)        # returns 3
cache.get(4)        # returns 4
