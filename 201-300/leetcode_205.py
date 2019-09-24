class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        for i in range(len(s)):
            try:
                if dic1[s[i]] != t[i]:
                    return False
            except:
                dic1[s[i]] = t[i]
        l = list(dic1.values)
        if len(l) != len(set(l)):
            return False
        return True
