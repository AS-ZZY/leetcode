class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l = []
        for i in ops:
            if i == "D":
                if len(l) > 0:
                    l.append(l[-1] * 2)
            elif i == "C":
                if len(l) > 0:
                    l.pop()
            elif i == "+":
                l.append(l[-1] + l[-2])
            else:
                l.append(int(i))
        return sum(l)
