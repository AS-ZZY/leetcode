class Solution:
    def partition(self, s: str):
        l = []

        def huiwen(ss):
            for i in range(len(ss) // 2 + 1):
                if ss[i] != ss[len(ss) - 1 - i]:
                    return False
            return True

        if s == "":
            return [[]];

        for i in range(1, len(s) + 1):
            if huiwen( s[0 : i] ):
                z = self.partition(s[i:])
                for j in z:
                    j.insert(0, s[0 : i])
                    l.append(j)
        
        return l
