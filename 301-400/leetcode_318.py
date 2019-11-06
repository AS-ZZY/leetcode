class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = []
        for i in words:
            a = 0
            for j in set(i):
                a += 1 << (ord(j) - ord("a") )
            l.append(a)
        maxl = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if l[i] & l[j] == 0 and maxl < len(words[i]) * len(words[j]):
                    maxl = len(words[i]) * len(words[j])
        return maxl