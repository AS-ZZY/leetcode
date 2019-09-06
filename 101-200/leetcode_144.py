class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        list_1 = []
        list_2 = []
        p = root
        while p != None or len(list_2) != 0:
            if p != None:
                list_2.append(p)
                list_1.append(p.val)
                p = p.left
            else:
                p = list_2[-1].right
                list_2 = list_2[:-1]
        return list_1



