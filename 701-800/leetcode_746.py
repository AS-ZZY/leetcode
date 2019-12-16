class Solution:
    def minCostClimbingStairs(self, cost):
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 0:
            return 0
        minCost = [ cost[-2], cost[-1] ]
        print(minCost)
        for i in range(len(cost) - 3, -1, -1):
            a = minCost[0]
            minCost[0] = cost[i] + min(minCost)
            minCost[1] = a
        return min(minCost)