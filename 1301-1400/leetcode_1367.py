class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root is None:
            return False
        
        def start(root, head):
            if head == None:
                return True
            if root is None:
                return False
            if root.val == head.val:
                return start(root.left, head.next) or start(root.right, head.next)
            else:
                return False

        if root.val == head.val:
            if start(root, head):
                return True
        return self.isSubPath( head, root.left) or self.isSubPath(head, root.right)