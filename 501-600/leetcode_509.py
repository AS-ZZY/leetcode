class Solution:
    def fib(self, N: int):
        a = 0
        b = 1
        if N == 0:
            return 0
        if N == 1:
            return 1
        m = 1
        while m < N:
            m += 1
            c = a + b
            a = b
            b = c
        return b