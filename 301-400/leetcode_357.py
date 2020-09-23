class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            a = 81
            b = 91
            for i in range(3, n + 1):
                a *= (11 - i)
                b += a
        return b
