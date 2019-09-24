class Solution:
    def findPairs(self, nums, n: int) -> int:
        if k < 0:
            return 0
        nums = sorted(nums)
        i = 0
        j = 1
        num = 0
        while j < len(nums):
            if nums[j] - nums[i] < n:
                j += 1
            else:
                if nums[j] - nums[i] == n:
                    num += 1
                else:
                    j -= 1
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
                if j <= i:
                    j = i + 1    
        return num
