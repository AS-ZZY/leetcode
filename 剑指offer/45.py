class Solution:
    def minNumber(self, nums: list) -> str:
        c = True
        nums = list(map(str, nums))
        while c:
            c = False
            for i in range(len(nums) - 1):
                a = nums[i] + nums[i + 1]
                b = nums[i + 1] + nums[i]
                if int(a) > int(b):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    c = True
        s = ""
        for i in nums:
            s += i
        return s
