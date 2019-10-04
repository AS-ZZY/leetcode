class Solution:
    def findAnagrams(self, s: str, p: str):
        l = []
        dic = {}
        for i in p:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        start = 0
        dic2 = dic.copy()
        for i in range(len(s)):
            try:
                dic2[s[i]] -= 1
                if dic2[s[i]] == -1:
                    for j in range(start, i):
                        dic2[s[j]] += 1
                        if s[j] == s[i]:
                            start = j + 1
                            break
            except:
                start = i + 1
                dic2 = dic.copy()
            if i - start == len(p) - 1:
                l.append(start)
        return l
