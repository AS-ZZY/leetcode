class Solution:
    def removeDuplicates(self, S: str) -> str:
        l = []
        for i in S:
            if len(l) > 0 and l[-1] == i:
                l.pop()
            else:
               l.append(i)
        l = "".join(l)
        return l