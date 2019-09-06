class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = []
        i = 0
        while i < len(nums):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                a = nums[i] + nums[start] + nums[end]
                if a > 0:
                    end -= 1
                elif a < 0:
                    start += 1
                else:
                    l.append([nums[i], nums[start], nums[end]])
                    while end > start and nums[end - 1] == nums[end]:
                        end -= 1
                    end -= 1
            while i + 1< len(nums) and nums[i + 1] == nums[i]: 
                i += 1
            i += 1
        return l
