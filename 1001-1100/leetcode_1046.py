from collections import Counter


class Solution:
    def lastStoneWeight(self, stones):
        dic = dict(Counter(stones))
        a = list(dic.keys())
        a.sort(reverse=True)
        while True:
            m = a[0]
            if dic[m] % 2 == 0:
                if len(a) == 1:
                    return 0
                a = a[1:]
            else:
                if len(a) == 1:
                    return m
                n = m - a[1]
                dic[a[1]] -= 1
                if dic[a[1]] == 0:
                    a = a[2:]
                else:
                    a = a[1:]
                if len(a) == 0:
                    return n
                add = False
                for k in range(len(a)):
                    if n < a[k]:
                        pass
                    elif n == a[k]:
                        add = True
                        dic[a[k]] += 1
                        break
                    else:
                        add = True
                        a.insert(k, n)
                        dic[n] = 1
                        break
                if not add:
                    a.append(n)
                    dic[n] = 1
