class Solution:
    def equationsPossible(self, equations) -> bool:
        def find(x):
            if x == p[x]:
                return p[x]
            else:
                p[x] = find(p[x])
                return p[x]
        
        p = [i for i in range(26)]

        for eq in equations:
            if eq[1] == '=':
                r1 = find(ord(eq[0]) - ord('a'))        
                r2 = find(ord(eq[3]) - ord('a'))
                if r1!= r2:
                    p[r2] = r1

        for eq in equations:
            if eq[1] == '!':
                r1 = find(ord(eq[0]) - ord('a'))        
                r2 = find(ord(eq[3]) - ord('a'))
                if r1== r2:
                    return False
        return True