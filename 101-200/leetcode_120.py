class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        l = [triangle[0][0]]
        for i in range(1, len(triangle)):
            ll = []
            for j in range(len(l)):
                if j == 0:
                    a = l[0] + triangle[i][0]
                else:
                    a = min([l[j - 1] + triangle[i][j], l[j] + triangle[i][j]])
                ll.append(a)
            a = triangle[i][-1] + l[-1]
            ll.append(a)
            l = ll.copy()
        return min(l)
