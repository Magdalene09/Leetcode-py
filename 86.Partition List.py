# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesserHalf = ListNode(-1)
        greaterHalf = ListNode(-1)

        lPtr = lesserHalf
        gPtr = greaterHalf

        curPtr = head

        while curPtr :
            if curPtr.val < x :
                lPtr.next = curPtr
                lPtr = lPtr.next

            else :
                gPtr.next = curPtr
                gPtr = gPtr.next

            curPtr = curPtr.next

        lPtr.next = greaterHalf.next
        gPtr.next = None

        return lesserHalf.next
