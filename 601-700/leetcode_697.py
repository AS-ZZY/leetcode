from collections import Counter 

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = dict(Counter(nums))
        a = max(dic.values())
        l = [ v[0] for v in dic.items() if v[1] == a ]
        minIndex = len(nums)
        for i in l:
            start = nums.index(i)
            end = len(nums) - nums[::-1].index(i) - 1
            if minIndex > end - start:
                minIndex = end - start
        return minIndex