class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def in_order(node, res):
            if node is None:
                return
            if node.left:
                in_order(node.left, res)
            res.append(node.val)
            if node.right:
                in_order(node.right, res)
            return res

        res1 = in_order(root1, [])
        res2 = in_order(root2, [])
        result = []
        if not res1:
            return res2
        if not res2:
            return res1
        i = 0
        j = 0
        while i < len(res1) or j < len(res2):
            if i < len(res1) and j < len(res2):
                if res1[i] < res2[j]:
                    result.append(res1[i])
                    i += 1
                else:
                    result.append(res2[j])
                    j += 1
            elif i < len(res1):
                result.append(res1[i])
                i += 1
            else:
                result.append(res2[j])
                j += 1
        return result
