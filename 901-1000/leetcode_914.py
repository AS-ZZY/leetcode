from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck):
        value = list(dict(Counter(deck)).values())
        for i in range(2, min(value) + 1):
            T = False
            for j in value:
                if j % i == 0:
                    T = True
                else:
                    T = False
                    break
            if T:
                return True
        return False