class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        while True:
            t = 10 ** (i - 1)
            m = i * 9 * t
            if n <= m:
                n -= 1
                return int(str(t + n // i)[n % i])
            n -= m
            i += 1
