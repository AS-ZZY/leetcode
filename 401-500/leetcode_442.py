class Solution:
    def findDuplicates(self, nums):
        re = []
        n = len(nums)
        for i in range(n):
            nums[(nums[i] - 1) % n] += n
        for i in range(n):
            if nums[i] > 2 * n:
                re.append(i + 1)
        return re
