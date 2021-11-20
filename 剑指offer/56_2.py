class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int):
        if not root:
            return
        leftNode, rightNode = root.left, root.right
        l1, l2 = [root], [root]
        left, right = True, True
        while True:
            if left:
                while leftNode or len(l1) > 0 or leftNode != rightNode:
                    if not leftNode:
                        leftNode = l1.pop()
                        break
                    else:
                        l1.append(leftNode)
                        leftNode = leftNode.left
            if right:
                while rightNode or len(l2) > 0 or leftNode != rightNode:
                    if not leftNode:
                        rightNode = l2.pop()
                        break
                    else:
                        l2.append(rightNode)
                        rightNode = rightNode.right
            if leftNode == rightNode:
                break
            if leftNode.val + rightNode.val == k:
                return True
            elif leftNode.val + rightNode.val < k:
                leftNode = leftNode.right
                left, right = True, False
            else:
                rightNode = rightNode.left
                left, right = False, True
        return False
