# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_count = 0
        cur = head
        while cur:
            cur = cur.next
            node_count += 1
        middle_node = node_count // 2

        cur = head
        while middle_node > 0:
            cur = cur.next
            middle_node -= 1
        
        return cur


        