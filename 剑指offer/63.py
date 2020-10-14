class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        maxV = 0
        minV = prices[0]
        for i in range(1, len(prices)):
            if minV > prices[i]:
                minV = prices[i]
            elif maxV < prices[i] - minV:
                maxV = prices[i] - minV
        return maxV