class Solution:
    def constructRectangle(self, area: int):
        a = int(area ** 0.5)
        while a > 0:
            if area % a == 0:
                return [area // a, a]
            a -= 1
