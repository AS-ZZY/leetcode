class Solution:
    def reverseWords(self, s: str):
        l = s.split(" ")
        ll = []
        for i in l:
            if i:
                ll.append(i)
        return " ".join(ll[::-1])