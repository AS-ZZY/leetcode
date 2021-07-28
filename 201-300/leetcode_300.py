class Solution:
    def lengthOfLIS(self, nums):
        re = []
        for i in range(len(nums)):
            m = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    m = max(re[j] + 1, m)
                elif nums[j] == nums[i]:
                    m = max(m, re[j])
            if m == 0:
                m = 1
            re.append(m)
        return max(re)
