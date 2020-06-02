class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_ = max(candies)
        l = []
        for i in candies:
            if i + extraCandies >= max_:
                l.append(True)
            else:
                l.append(False)
        return l