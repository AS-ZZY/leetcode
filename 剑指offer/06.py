class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        s = head
        while s:
            l.append(s.val)
            s = s.next
        return l[::-1]