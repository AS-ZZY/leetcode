class Solution:
    def subsets(self, nums):
        l1 = [[]]
        for i in nums:
            l2 = []
            for j in l1:
                jj = j.copy()
                l2.append(jj)
                j.append(i)
                l2.append(j)
            l1 = l2.copy()
        return l1


a = Solution()
l = [1, 2, 3]
print(a.subsets(l))
