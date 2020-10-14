class Solution:
    def findContinuousSequence(self, target: int):
        i = 1
        sums = 0
        l = []
        re = []
        add = True
        while i <= int(target / 2) + 1:
            if add:
                sums += i
                l.append(i)
            if sums == target:
                re.append(l.copy())
                sums -= l[0]
                l = l[1:]
                add = True
                i += 1
            elif sums > target:
                sums -= l[0]
                l = l[1:]
                add = False
            else:
                add = True
                i += 1
        return re