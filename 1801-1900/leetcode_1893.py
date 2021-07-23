class Solution:
    def isCovered(self, ranges, left: int, right: int):
        ranges.sort(key=lambda x: x[0])
        l = [ranges[0]]
        for i in range(1, len(ranges)):
            r = ranges[i]
            if r[0] > l[-1][1]:
                l.append(r)
            else:
                l[-1] = [l[-1][0], max(l[-1][1], r[1])]
        index, i = 0, left
        while i <= right:
            if i > l[index][1]:
                index += 1
                if index == len(l):
                    return False
            elif i < l[index][0]:
                return False
            else:
                i += 1
        return True
