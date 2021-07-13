from collections import Counter


class Solution:
    def countPairs(self, deliciousness):
        kk = 10 ** 9 + 7
        dic = dict(Counter(deliciousness))
        l = list(dic.keys())
        m = max(l)
        n = 1
        ll = []
        while n <= m * 2:
            ll.append(n)
            n = n << 1
        num = 0
        for i in l:
            for j in ll:
                try:
                    if j < i << 1:
                        continue
                    dic[j - i]
                    if j == i << 1:
                        num += (((dic[i] - 1) * dic[i]) // 2) % kk
                    else:
                        num += (dic[i] * dic[j - i]) % kk
                    num = num % kk
                except:
                    pass
        return num
