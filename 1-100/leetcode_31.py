class Solution:
    def nextPermutation(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        nums[i:] = nums[i:][::-1]
                        return
        i, j = 0, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
