class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def getRest(x):
            s = ""
            for i in range(len(x)):
                if x[i] == "1":
                    s = s + "0"
                else:
                    s = s + "1" + x[i + 1:]
                    return s
            return s + "1"

        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        a = a[::-1]
        b = b[::-1]
        i = 0
        c = ""
        tar = 0
        while i < len(a) and i < len(b):
            s = int(a[i]) + int(b[i]) + tar
            if s < 2:
                tar = 0
                c = c + str(s)
            else:
                tar = 1
                c = c + str(s - 2)
            i += 1
        if i < len(a):
            if tar == 1:
                c = c + getRest(a[i :])
            else:
                c = c + a[i:]
        elif i < len(b):
            if tar == 1:
                c = c + getRest(b[i :])
            else:
                c = c + b[i:]
        elif tar == 1:
            c = c + "1"
        return c[::-1]