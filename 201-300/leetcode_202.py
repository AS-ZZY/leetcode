class Solution:
    def isHappy(self, n: int) -> bool:
        list_ = []
        k = n
        while True:
            sum_ = 0
            while k > 0:
                a = k % 10
                sum_ += a ** 2
                k = k // 10
            if sum_ == 1:
                return True
            if sum_ in list_:
                return False
            else:
                list_.append(sum_)
                k = sum_
