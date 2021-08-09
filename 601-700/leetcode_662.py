class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode):
        if not root:
            return 0
        root.num = 0
        l1, maxWidth = [root], 1
        while True:
            l2 = []
            for i in l1:
                if i.left:
                    i.left.num = 2 * i.num
                    l2.append(i.left)
                if i.right:
                    i.right.num = 2 * i.num + 1
                    l2.append(i.right)
            if len(l2) == 0:
                break
            width = l2[-1].num - l2[0].num + 1
            maxWidth = maxWidth if maxWidth > width else width
            l1 = l2
        return maxWidth
