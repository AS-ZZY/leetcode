class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        t1 = 'Fizz'
        t2 = 'Buzz'
        t3 = 'FizzBuzz'
        re = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                re.append(t3)
            elif i % 3 == 0:
                re.append(t1)
            elif i % 5 == 0:
                re.append(t2)
            else:
                re.append(str(i))
        return re
