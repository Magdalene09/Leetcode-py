# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseNodes(head) :
    curPtr = head
    prev = None

    while curPtr :
        temp = curPtr.next
        curPtr.next = prev
        prev = curPtr
        curPtr = temp

    return prev
  
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = reverseNodes(head)
        curPtr = head
        maxVal = float("-inf")

        dummyNode = ListNode(-1)
        dPtr = dummyNode

        while curPtr :
            if curPtr.val >= maxVal :
                dPtr.next = curPtr
                dPtr = dPtr.next
                maxVal = curPtr.val
            
            curPtr = curPtr.next
        
        dPtr.next = None

        return reverseNodes(dummyNode.next)
