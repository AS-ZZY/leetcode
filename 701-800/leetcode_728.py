class Solution:
    def selfDividingNumbers(self, left, right):
        is_div_num = lambda n: not any([n % int(b) if b != '0' else 1 for b in list(str(n))])
        return [n for n in range(left, right+1) if is_div_num(n)]