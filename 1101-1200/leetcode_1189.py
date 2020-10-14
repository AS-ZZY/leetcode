from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = dict(Counter(list(text)))
        dic2 = dict(Counter(list("balloon")))
        mintimes = float("inf")
        for i in dic2.keys():
            try:
                s = int(dic[i] / dic2[i])
                if mintimes > s:
                    mintimes = s
            except:
                return 0
        return mintimes