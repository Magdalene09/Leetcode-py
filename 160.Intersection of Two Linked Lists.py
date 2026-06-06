# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        aPtr = headA
        bPtr = headB

        while aPtr != bPtr :
            aPtr = aPtr.next
            bPtr = bPtr.next

            if aPtr == bPtr : return aPtr

            if not aPtr : aPtr = headB
            if not bPtr : bPtr = headA

        return aPtr
