class Solution:
    def missingNumber(self, nums):
        result = 0
        for i in range(len(nums)):
            result ^= ( i ^ nums[i] )
        result ^= len(nums)
        return result