class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        num = sorted(nums)
        m = float("inf")
        l = 0
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start != end:
                if start >= len(nums):
                    break
                p = nums[start] + nums[end] + nums[i]
                a = target - p
                if m > abs(a):
                    m = abs(a)
                    l = p
                if a == 0:
                    return target
                elif a < 0:
                    end -= 1
                else:
                    start += 1
        return l
