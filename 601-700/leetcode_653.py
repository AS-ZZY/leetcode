class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int):
        dic = {}
        l, p = [], root
        while p or len(l) > 0:
            if not p:
                p = l.pop()
                p = p.right
            else:
                try:
                    dic[k - p.val]
                    return True
                except:
                    dic[p.val] = 1
                l.append(p)
                p = p.left
        return False
