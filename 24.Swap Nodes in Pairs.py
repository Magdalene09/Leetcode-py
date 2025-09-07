# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        cur=head


        while cur and cur.next:
            first=cur
            second=cur.next
            temp=second.next
          
            prev.next=second
            second.next=first
            first.next=temp
            prev=first
            cur=temp

        return dummy.next

       
