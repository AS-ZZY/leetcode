class Solution:
    def largestNumber(self, nums):
        nums = [ str(i) for i in nums ]
        change = True
        while change:
            change = False
            for i in range(len(nums) - 1):
                a = nums[i] + nums[i + 1]
                b = nums[i + 1] + nums[i]
                for j in range(len(a)):
                    if int(a[j]) > int(b[j]):
                        break
                    elif int(a[j]) < int(b[j]):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        change = True                      
                        break
        a = "".join(nums)
        i = 0
        while i < len(a):
            if a[i] != "0":
                return a[i:]
            i += 1
        return "0"