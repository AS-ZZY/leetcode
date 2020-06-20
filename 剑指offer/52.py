class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headA and headB):
            return None
        len1 = 1
        len2 = 1
        p = headA
        while p:
            p = p.next
            len1 += 1
        p = headB
        while p:
            p = p.next
            len2 += 1
        q = None
        l = 0
        if len2 > len1:
            p = headA
            q = headB
            l = len2 - len1
        else:
            p = headB
            q = headA
            l = len1 - len2
        i = 0
        while i < l:
            i += 1
            q = q.next
        while p is not q and p is not None:
            p = p.next
            q = q.next
        return p