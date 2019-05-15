class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l_1 = sorted(nums[0:3])
        l_2 = sorted(nums[0:3])[0:2]
        for i in range(3, len(nums)):
            if nums[i] > l_1[0]:
                l_1[0] = nums[i]
                l_1 = sorted(l_1)
            elif nums[i] < l_2[1]:
                l_2[1] = nums[i]
                l_2 = sorted(l_2)
        a = l_1[0] * l_1[1] * l_1[2]
        b = l_1[2] * l_2[0] * l_2[1]
        print(l_1)
        print(l_2)
        if a > b:
            return a
        return b

            
            