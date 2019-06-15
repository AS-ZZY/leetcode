class Solution:
    def compareVersion(self, version1: str, version2: str):
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        l = min(len(v1), len(v2))
        for i in range(l):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        if len(v1) == len(v2):
            return 0
        elif len(v1) > l:
            li = v1[l:]
            a = 1
        else:
            li = v2[l:]
            a = -1
        for i in li:
            if i != 0:
                return a
        return 0
        