class Solution:
    def generateParenthesis(self, n: int):
        l = []
        re = []
        self.start(l, n, n, re)
        return re

    def start(self, l, n1, n2, re):
        if n2 == 0:
            re.append(l)
            return
        if n1 < n2:
            if n1 > 0:
                self.start(l + ["("], n1 - 1, n2, re)
            self.start(l + [")"], n1, n2 - 1, re)
        else:
            self.start(l + ["("], n1 - 1, n2, re)

