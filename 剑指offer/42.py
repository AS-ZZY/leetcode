class Solution:
    def maxSubArray(self, nums):
        result = nums[0]
        m = 0
        for i in range(len(nums)):
            d = m + nums[i]
            if d < 0:
                m = 0
                if result < 0 and result < nums[i]:
                    result = nums[i]
            else:
                m = d
                if result < m:
                    result = m
        return result