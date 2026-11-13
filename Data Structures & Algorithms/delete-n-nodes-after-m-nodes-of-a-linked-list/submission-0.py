# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        keep = m 
        skip = n
        dummy = ListNode(0, None)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if m > 0:
                cur = cur.next
                m -= 1
            elif m==0:
                while n > 0 and cur.next:
                    cur.next = cur.next.next
                    n -= 1
                n = skip
                m = keep
        return dummy.next
