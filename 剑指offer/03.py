from collections import Counter

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = dict(Counter(nums))
        for i in dic:
            if dic[i] > 1:
                return i