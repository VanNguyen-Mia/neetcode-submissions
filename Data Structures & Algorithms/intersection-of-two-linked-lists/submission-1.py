# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer1 = headA
        pointer2 = headB

        count1 = count2 = 1
        while pointer1 and pointer2 and count1 >= 0 and count2>=0:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer1 == None:
                pointer1 = headB
                count1 -= 1
            if pointer2 == None:
                pointer2 = headA
                count2 -= 1
            if pointer1 == pointer2:
                return pointer1
        return None