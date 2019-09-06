class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0     
        else:
            result = [1] * n
            result[0], result[1] = 0, 0
            for i in range(2, int(n**0.5)+1): 
                if result[i] == 1:
                    result[i*i:n:i] = [0] * len(result[i*i:n:i])
        return sum(result)
