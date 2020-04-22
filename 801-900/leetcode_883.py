class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        num = 0
        for i in range(len(grid)):
            num += max(grid[i])
        for i in range(len(grid)):
            max_ = 0
            for j in range(len(grid)):
                if max_ < grid[j][i]:
                    max_ = grid[j][i]
                if grid[j][i] != 0:
                    num += 1
            num += max_
        return num