class Solution:
    def exchange(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 1:
                i += 1
            else:
                a = nums[i]
                nums[i] = nums[j]
                nums[j] = a
                j -= 1
        return nums