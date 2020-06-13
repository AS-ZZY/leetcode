class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                return head
            p = p.next