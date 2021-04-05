class Solution:
    def findJudge(self, N: int, trust):
        dic1 = {}
        dic2 = {}
        for i in range(1, N + 1):
            dic1[i] = 1
            dic2[i] = []
        for i in trust:
            dic1[i[0]] = 0
            dic2[i[1]].append(i[0])
        for i in range(1, N + 1):
            if dic1[i] == 1:
                if len(list(set(dic2[i]))) == N - 1:
                    return i
        return -1
