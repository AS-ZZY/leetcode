from collections import Counter


class Solution:
    def findLHS(self, nums):
        dic = dict(Counter(nums))
        dic = dict(sorted(dic.items(), key=lambda item:item[0]))
        keys = list(dic.keys())
        max_ = 0
        for i in range(1, len(keys)):
            if keys[i] - 1 == keys[i - 1]:
                m = dic[keys[i]] + dic[keys[i - 1]]
                if max_ < m:
                    max_ = m
        return max_