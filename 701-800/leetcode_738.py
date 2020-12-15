class Solution:
    def monotoneIncreasingDigits(self, N: int):
        while True:
            l = list(map(int, list(str(N))))
            for i in range(len(l) - 1, 0, -1):
                if l[i] < l[i - 1]:
                    l[i - 1] -= 1
                    for j in range(i, len(l)):
                        l[j] = 9
            l = list(map(str, l))
            l = "".join(l)
            return int(l)
