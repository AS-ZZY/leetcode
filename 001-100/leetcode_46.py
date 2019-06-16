class Solution:
    def permute(self, nums):
        l = []
        re = []
        self.start(l, nums, re)
        return re

    def start(self, l, nums, re):
        if len(nums) == 0:
            re.append(l)
        for i in range(len(nums)):
            self.start(l +[nums[i]], nums[0:i] + nums[i + 1:], re) 
        