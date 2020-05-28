class Solution:
    def decodeString(self, s):
        left = -1
        for i in range(len(s)):
            if s[i] == "[":
                left = i
            if s[i] == "]":
                a = ""
                j = left - 1
                while j >= 0:
                    try:
                        int(s[j] + a)
                        a = s[j] + a
                    except:
                        break
                    j -= 1
                re = ""
                if j >= 0:
                    re = s[:j + 1]
                re = re + int(a) * s[left + 1:i] + s[i + 1:]
                return self.decodeString(re)
        return s   