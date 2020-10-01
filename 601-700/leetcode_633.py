class Solution:
    def judgeSquareSum(self, c: int):
        for i in range(0, int(c ** 0.5) + 1):
            b = c - i * i
            a = b ** 0.5
            if a == int(a):
                return True
        return False
