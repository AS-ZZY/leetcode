from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = Counter(list(s))
        dic2 = Counter(list(t))
        if len(dic1.keys()) != len(dic2.keys()):
            return False
        for i in dic1.keys():
            try:
                if dic1[i] != dic2[i]:
                    return False
            except:
                return False
        return True