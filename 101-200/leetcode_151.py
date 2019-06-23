class Solution(object):
    def reverseWords(self, s):
        if s == "":
            return ""
        l = ''
        start = -1
        end = -1
        for i in range(len(s)):
            if self.isletter(s[i]) and start == -1:
                start = i
            if not self.isletter(s[i]) and start != -1:
                end = i
            if start != -1 and end != -1:
                l = s[start: end] + " " + l
                start = -1
                end = -1
        if start != -1 and end == -1:
            l = s[start:] + " " + l
        return l[:-1]
        
    def isletter(self, m):
        if m == " ":
            return False
        return True