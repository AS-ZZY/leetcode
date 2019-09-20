class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        l = preorder.split(",")
        num = 1
        for i in range(len(l)):
            if l[i] != "#":
                if num == 0:
                    return False
                num += 1
            else:
                num -= 1
                if num < 0:
                    break
        if num == 0:
            return True
        else:
            return False
