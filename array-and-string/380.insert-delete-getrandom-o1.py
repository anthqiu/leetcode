"""
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

import random


class RandomizedSet:

    def __init__(self):
        self.data = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.data.append(val)
        self.idx_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            idx = self.idx_map[val]
            # swap item at idx and the last item
            last_data = self.data[-1]
            self.data[idx] = last_data
            self.idx_map[last_data] = idx
            # remove the last item which is now useless
            self.data.pop()
            self.idx_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
