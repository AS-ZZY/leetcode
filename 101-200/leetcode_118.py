class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        li = [[1]]
        i= 1
        while i < numRows:
            l = li[-1].copy()
            for j in range(len(l) - 1,0,-1):
                l[j] = l[j] + l[j - 1]
            l.append(1)
            li.append(l)
            i += 1
        return li
