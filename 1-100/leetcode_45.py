class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        step = 0
        n = nums[0]
        a = len(nums)
        r = 0
        for i in range(a):
            n = max(n, i + nums[i])            
            if i + nums[i] >= a - 1:
                return step + 1
            if r == i:
                step += 1
                r = n
        return step
