class Solution:
    def permuteUnique(self, nums):
        l = []
        re = []
        self.start(l, nums, re)
        return re

    def start(self, l, nums, re):
        if len(nums) == 0:
            re.append(l)
            return
        z = []
        for i in range(len(nums)):
            if nums[i] not in z:
                self.start(l + [nums[i]], nums[0:i] + nums[i + 1:], re) 
                z.append(nums[i]) 