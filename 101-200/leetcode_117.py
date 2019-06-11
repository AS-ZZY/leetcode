class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node'):
        if root is None:
            return
        l = [root]
        while len(l) != 0:
            for i in range(0, len(l) - 1):
                l[i].next = l[i + 1]
            l[-1].next = None
            l = self.start(l)
        return root
            


    def start(self, l):
        l2 = []
        for i in l:
            if i.left is not None:
                l2.append(i.left)
            if i.right is not None:
                l2.append(i.right)
        return l2