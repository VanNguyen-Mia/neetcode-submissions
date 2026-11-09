# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        values = []

        cur = head
        while cur:
            values.append(cur)
            if cur.next in values:
                return True
            cur = cur.next
        return False