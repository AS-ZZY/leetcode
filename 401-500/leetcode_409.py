class Solution:
    def longestPalindrome(self, s: str):
        l = []
        num = 0
        for i in s:
            if i in l:
                num += 1
                l.remove(i)
            else:
                l.append(i)
        if num * 2 < len(s):
            return num * 2 + 1
        else:
            return num * 2