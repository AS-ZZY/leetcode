class Solution:
    def largestRectangleArea(self, heights):
        l = [-1]
        heights.append(0)
        maxArea = 0
        for i in range(len(heights)):
            while len(l) > 1:
                if heights[l[-1]] > heights[i]:
                    if maxArea < heights[l[-1]] * (i - l[-2] - 1):
                        maxArea = heights[l[-1]] * (i - l[-2] - 1)
                    l.pop()
                else:
                    break
            l.append(i)
        return maxArea