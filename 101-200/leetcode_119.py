class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        for i in range(-1,rowIndex):
            for j in range(len(l) - 1, 0, -1):
                l[j] = l[j] + l[j - 1]
            l.append(1)
        return l