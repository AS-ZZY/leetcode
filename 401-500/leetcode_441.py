class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        level = 0
        while n >= i:
            n -= i
            i += 1
            level += 1
        return level
