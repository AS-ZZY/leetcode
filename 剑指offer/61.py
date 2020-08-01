class Solution:
    def isStraight(self, nums):
        num = sorted(nums)
        l0 = len([i for i in num if i == 0 ])
        num = num[l0:]
        isS = True
        for i in range(len(num)):
            if num[i] == num[i + 1] - 3:
                if l0 == 2:
                    l0 = 0
                else:
                    isS = False
                    break
            elif num[i] == num[i + 1] - 2:
                if l0 > 0:
                    l0 -= 1
                else:
                    isS = False
                    break
            elif num[i] != num[i + 1] - 1:
                isS = False
                break
        return isS

C = Solution()
num = [0,0,1,2,5]
print(C.isStraight(num))