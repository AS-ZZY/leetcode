class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while True:
            middle = (start + end) // 2
            if end == start or end - 1 == start:
                return nums[end] if nums[end] < nums[start] else nums[start]
            if nums[middle] < nums[end]:
                end = middle
            else:
                start = middle
