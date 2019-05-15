class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        res1, res2 = None, None
        res = []
        for num in nums:
            if count1 == 0 and num != res2:
                count1 = 1
                res1 = num
                continue
            elif count2 == 0 and num != res1:
                count2 = 1
                res2 = num
                continue
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
        if count1 > len(nums)/3:
            res.append(res1)
        if count2 > len(nums)/3:
            res.append(res2)
        return res
        