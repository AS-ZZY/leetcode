class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return []
        re = [chars[0]]
        j = 1
        num = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i - 1]:
                num += 1
            else:
                if num != 1:
                    s = str(num)
                    for k in s:
                        chars[j] = k
                        j += 1
                    num = 1
                chars[j] = chars[i]
                j += 1
        if num != 1:
            s = str(num)
            for k in s:
                chars[j] = k
                j += 1
        return j
