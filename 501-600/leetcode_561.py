class Solution:
    def arrayPairSum(self, nums) -> int:
        nums = sorted(nums)
        num = 0
        for i in range(0, len(nums), 2):
            num += nums[i]
        return num
