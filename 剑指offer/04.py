class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int):
        if len(matrix) == 0:
            return False
        left, right = 0, len(matrix[0]) - 1
        while left < len(matrix) and right >= 0:
            a = matrix[left][right]
            if a < target:
                left += 1
            elif a > target:
                right -= 1
            else:
                return True
        return False