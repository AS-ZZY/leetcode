class Solution:
    def tribonacci(self, n: int):
        n0, n1, n2 =0, 1, 1
        if n == 0:
            return 0
        if n < 3:
            return 1
        t = 2
        while t < n:
            n0, n1, n2 = n1, n2, n0 + n1 + n2
            t += 1
        return n2
