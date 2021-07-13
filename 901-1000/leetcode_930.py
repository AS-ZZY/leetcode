class Solution:
    def numSubarraysWithSum(self, nums, goal):
        l = []
        for i in range(len(nums)):
            if nums[i] == 1:
                l.append(i)
        if len(l) < goal:
            return 0
        l = [-1] + l
        l.append(len(nums))
        num = 0
        if goal == 0:
            for i in range(1, len(l)):
                a = l[i] - l[i - 1] - 1
                num += (1 + a) * a // 2
            return num
        for i in range(1, len(l) - goal):
            j = i + goal - 1
            num += (l[i] - l[i - 1]) * (l[j + 1] - l[j])
        return num
