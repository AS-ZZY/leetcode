class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        if root is None:
            return []
        return self.s(root)

        
    def s(self, root):
        re = []
        for i in root.children:
            re = re + self.s(i)
        re.append(root.val)
        return re


            
