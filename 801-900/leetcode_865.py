class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, node=None):
        self.node = node
        self.num = 1


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode):
        l = []
        num = 1
        deep = -1
        if not root:
            return root
        p = Tree(root)
        r = []
        none = Tree(None)
        while len(r) > 0 or p.node:
            if p.node:
                r.append(p)
                num += 1
                p = Tree(p.node.left)
            else:
                q = r[-1]
                if q.num == 1:
                    q.num = 2
                    if not q.node.right and not q.node.left:
                        if deep < num:
                            deep = num
                            l = [r.copy()]
                        elif deep == num:
                            l.append(r.copy())
                    else:
                        p = Tree(q.node.right)
                else:
                    num -= 1
                    r.pop()
        i = 0
        t = True
        if len(l) == 1:
            return l[-1].node
        while t:
            i += 1
            if i > len(l[0]):
                break
            p = l[0][i]
            for j in l[1:]:
                if i > len(j) or p != j[i]:
                    t = False
                    break
        return l[0][i - 1].node
