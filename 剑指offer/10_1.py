class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return 0
        i = 1
        while i < n:
            i += 1
            a, b = b, a + b
        return  b % (10 ** 9 + 7)