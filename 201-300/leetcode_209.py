class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s > sum(nums):
            return 0
        left, right, res, sum_lr = 0, 0, len(nums)+1, 0  # 双指针都从第一位出发
        while right < len(nums):
            while sum_lr < s and right < len(nums):  # sum_lr小则右指针右移
                sum_lr += nums[right]
                right += 1
            while sum_lr > =s and left >= 0:  # sum_lr大则左指针右移
                res = min(res, right-left)
                sum_lr -= nums[left]
                left += 1
        return res
