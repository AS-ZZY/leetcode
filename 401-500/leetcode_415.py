class Solution:
    def addStrings(self, num1: str, num2: str):
        i = len(num1) - 1
        j = len(num2) - 1
        a = 0
        l = ''
        while i >= 0 and j >= 0:
            a = int(num1[i]) + int(num2[j]) + a
            if a >= 10:
                l = str(a - 10) + l
                a = 1
            else:
                l = str(a) + l
                a = 0
            i -= 1
            j -= 1
        while i >= 0:
            a = int(num1[i]) + a
            if a >= 10:
                l = str(a - 10) + l
                a = 1
            else:
                l = str(a) + l
                a = 0
                l = num1[:i]+ l
                break
            i -= 1
        while j >= 0:
            a = int(num2[j]) + a
            if a >= 10:
                l = str(a - 10) + l
                a = 1
            else:
                l = str(a) + l
                l = num2[:j] + l
                a = 0
                break
            j -= 1
        if a == 1:
            l = "1" + l
        return l