class Solution:
    def findRelativeRanks(self, nums):
        a = sorted(nums, reverse = True)
        dic = {}
        for i in range(len(a)):
            dic[a[i]] = i + 1
        l = []
        for i in nums:
            if dic[i] > 3:
                l.append(str(dic[i]))
            else:
                s = ["Gold Medal", "Silver Medal", "Bronze Medal"]
                l.append(s[dic[i] - 1])
        return l