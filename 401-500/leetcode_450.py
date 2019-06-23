class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        p = root
        l = None
        while p is not None:
            if p.val < key:
                l = p
                p = p.right
            elif p.val > key:
                l = p
                p = p.left
            else:
                break
        if p is None:
            return root
        if root.val == key and root.left is None and root.right is None:
            return None
        else:
            if p.right is None and p.left is None:
                if l.left == p:
                    l.left = None
                else:
                    l.right = None
            elif p.left is None:
                q = p.right
                if q.left is None:
                    p.val = q.val
                    p.right = q.right
                else:
                    while q.left.left is not None:
                        q = q.left
                    p.val = q.left.val
                    q.left = q.left.right
            else:
                q = p.left
                if q.right is None:
                    p.val = q.val
                    p.left = q.left
                else:
                    while q.right.right is not None:
                        q = q.right
                    p.val = q.right.val
                    q.right = q.right.left
            return root