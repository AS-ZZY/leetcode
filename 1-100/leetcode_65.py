class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            key=float(s)
            return True
        except:
            return False
