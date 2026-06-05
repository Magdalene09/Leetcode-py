# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return None

        fastPtr = head
        slowPtr = head
        fastPtr = fastPtr.next.next

        while fastPtr and fastPtr.next :
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        slowPtr.next = slowPtr.next.next

        return head
