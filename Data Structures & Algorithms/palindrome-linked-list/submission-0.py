# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        n = len(values) - 1
        for i in range(len(values)//2):
            if values[i] != values[n - i]:
                return False
        return True

