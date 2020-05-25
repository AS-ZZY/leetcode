class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sums = {0: 1}
        pre = 0
        t = 0
        for num in nums:
            pre += num
            try:
                t += sums[pre-k]
            except:
                pass
            try:
                sums[pre] += 1
            except:
                sums[pre] = 1
        return t