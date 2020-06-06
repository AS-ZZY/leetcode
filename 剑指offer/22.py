class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i = 1
        p = head
        while i < k:
            if p is None:
                return None
            i += 1
            p = p.next
        q = head
        while not p.next is None:
            p = p.next
            q = q.next
        return q
