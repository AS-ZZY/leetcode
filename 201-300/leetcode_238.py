class Solution:
    def productExceptSelf(self, nums):
        left = []
        right = []
        l = 1
        for i in nums:
            left.append(l)
            l *= i
        l = 1
        for i in range(len(nums) - 1, -1, -1):
            right.append(l)
            l *= nums[i]
        re = []
        for i in range(len(left)):
            re.append(left[i] * right[len(left) - 1 - i])
        return re
