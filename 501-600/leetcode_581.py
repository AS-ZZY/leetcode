class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2 and sorted_nums[p1] == nums[p1]:
            p1 += 1
        while p1 <= p2 and sorted_nums[p2] == nums[p2]:
            p2 -= 1
        return p2 - p1 + 1
