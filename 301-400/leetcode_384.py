import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        n = self.nums.copy()
        for i in range(len(self.nums)):
            a = random.randint(0, len(self.nums) - 1)
            n[i], n[a] = n[a], n[i]
        return n
