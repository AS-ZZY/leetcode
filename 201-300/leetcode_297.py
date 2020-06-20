class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[null]";
        l = [root]
        result = []
        while len(l) > 0:
            p = l[0]
            if p is None:
                result.append("null")
            else:
                result.append(str(p.val))
                l.append(p.left)
                l.append(p.right)
            l = l[1:]
        i = len(result) - 1
        while result[i] == "null":
            i -= 1
        result = result[:i + 1]
        return "[" + ",".join(result) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(",")
        if data[0] == "null":
            return None
        root = TreeNode(int(data[0]))
        l = [ root ]
        left = 0
        for i in data[1:]:
            if i == "null":
                if left == 1:
                    left = 0
                    l = l[1:]
                else:
                    left = 1
            else:
                p = TreeNode(int(i))
                if left == 0:
                    left = 1
                    l[0].left = p
                else:
                    left = 0
                    l[0].right = p
                    l = l[1:]
                l.append(p)
        return root