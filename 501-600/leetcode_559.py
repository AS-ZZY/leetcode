class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        l = [ root ]
        num = self.start(l)
        return num


    def start(self, l):
        childlist = []
        if len(l) == 0:
            return 0
        while True:
            if len(l) != 0:
                p = l.pop()
            else:
                break
            childlist.extend(p.children)
        return 1 + self.start(childlist)