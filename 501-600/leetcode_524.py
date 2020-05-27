class Solution:
    def findLongestWord(self, s: str, d) -> str:
        a = ""
        for i in d:
            if len(a) > len(i):
                continue
            if self.getSub(s, i):
                if len(a) < len(i):
                    a = i
                else:
                    if a > i:
                        a = i
        return a
            
            
    def getSub(self, a, b):
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                i += 1
            if len(a) - i < len(b) - j:
                break
        if j == len(b):
            return True
        return False
                            