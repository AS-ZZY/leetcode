class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = -1
        for i in s:
            j += 1
            while j < len(t):
                if i == t[j]:
                    break
                j += 1
            if j == len(t):
                return False
        return True
