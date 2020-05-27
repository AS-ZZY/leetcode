from collections import defaultdict

class Solution:
    def subarraysDivByK(self, A, K):
        dic = defaultdict(int)
        dic[0] = 1
        a = 0
        times = 0
        for i in A:
            a += i
            times += dic[a % K]
            dic[a % K] += 1
        return times