class Solution:
    def toGoatLatin(self, S):
        t = ""
        l = []
        start = 1
        yuan = ['a','e','i','o','u','A',"E","I","O","U"]
        l = S.split(" ")
        for i in l:
            if i[0] in yuan:
                t = t + i + "ma" + 'a' * start
            else:
                t = t + i[1:] + i[0] + "ma" + 'a' * start 
            start += 1
            t = t + " "
        return