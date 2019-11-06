class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        if len(nums) == 0:
            return l
        start = 0

        def getL(start, i):
            a = ""
            if start == i:
                a = str(nums[i])
            else:
                a = str(nums[start]) + "->" + str(nums[i])
            return a

        for i in range(len(nums)):
            if i == len(nums) - 1:
                l.append(getL(start, i))
            else:
                if nums[i] + 1 != nums[i + 1]:
                    l.append(getL(start, i))
                    start = i + 1
        return l