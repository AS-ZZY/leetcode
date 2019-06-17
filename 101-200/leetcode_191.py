class Solution(object):
    def hammingWeight(self, n):
        a = 1
        num = 0
        while a <= n:
            if a & n == a:
                num += 1
            a <<= 1
        return num