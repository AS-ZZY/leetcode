class Solution:
    def isValid(self, s: str):
        l = []
        for i in s:
            if i in ['(', "[", "{"]:
                l.append(i)
            else:
                if len(l) == 0:
                    return False
                a = l.pop()
                if i == ")" and a != '(':
                    return False
                if i == ']' and a != '[':
                    return False
                if i == '}' and a != '{':
                    return False
        if len(l) != 0:
            return False
        return True
