class Solution:
    def reverseParentheses(self, s):
        l = []
        re = ""
        i = 0
        while i < len(s):
            if s[i] == "(":
                l.append(i)
            elif s[i] == ")":
                start = l.pop()
                ss = s[start + 1: i][::-1]
                if len(l) == 0:
                    re += ss
                    s = s[i + 1:]
                    i = -1
                else:
                    s = s[:start] + ss + s[i + 1:]
                    i -= 2
            else:
                if len(l) == 0:
                    re += s[i]
            i += 1
        return re
