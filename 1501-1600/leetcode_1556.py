class Solution:
    def thousandSeparator(self, n: int):
        s = str(n)
        i = len(s) - 1
        num = 0
        while i > 0:
            num += 1
            if num == 3:
                num = 0
                s = s[:i] + "." + s[i:]
            i -= 1
        return s
