class Solution:
    def restoreArray(self, adjacentPairs):
        dic, re = {}, []
        for i in adjacentPairs:
            try:
                dic[i[0]].append(i[1])
            except:
                dic[i[0]] = [i[1]]
            try:
                dic[i[1]].append(i[0])
            except:
                dic[i[1]] = [i[0]]
        for i in dic.keys():
            if len(dic[i]) == 1:
                re = [i]
                break
        i, l = 1, len(dic.keys())
        while i < l:
            r = dic[re[i - 1]]
            if len(r) == 1:
                re.append(r[0])
            else:
                re.append(r[0] if r[0] != re[i - 2] else r[1])
            i += 1
        return re
