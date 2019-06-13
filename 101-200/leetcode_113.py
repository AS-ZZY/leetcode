class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def pathSum(self, root, sum):
        l2 = []
        if root is None:
            return []
        self.start(root, [], sum, l2)
        return l2
        
        
    def start(self, root, l, sum, l2):
        if root is None:
            return 
        l1 = l.copy()
        l1.append(root.val)
        if root.left is None and root.right is None and root.val == sum:
            l2.append(l1)
        else:
            self.start(root.left, l1, sum - root.val, l2)
            self.start(root.right, l1, sum - root.val, l2)

