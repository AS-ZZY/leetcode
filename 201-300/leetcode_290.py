class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ll = s.split(" ")
        dic = {}
        if len(pattern) != len(ll):
            return False
        for i in range(len(ll)):
            try:
                if dic[pattern[i]] != ll[i]:
                    return False
            except:
                dic[pattern[i]] = ll[i]
        l = list(dic.values())
        if len(l) != len(set(l)):
            return False
        return True
