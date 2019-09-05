class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        l = [1, 1, 2]
        s = 3
        while s <= n:
            m = l[s - 1] * 2
            frist = 1
            end = s - 2
            while frist < end:
                m += 2 * l[end] * l[frist]
                frist += 1
                end -= 1
            if frist == end:
                m += l[end] ** 2
            l.append(m)
            s += 1
        return l[-1]