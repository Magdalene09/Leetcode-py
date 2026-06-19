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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = reverseNodes(l1)
        l2 = reverseNodes(l2)

        fPtr = l1
        sPtr = l2
        carry = 0

        dummyNode = ListNode(-1)
        dPtr = dummyNode

        while fPtr or sPtr :
            val1 = fPtr.val if fPtr else 0
            val2 = sPtr.val if sPtr else 0
            totalSum = val1 + val2 + carry
            dPtr.next = ListNode(totalSum % 10)
            carry = totalSum // 10

            dPtr = dPtr.next
            if fPtr : fPtr = fPtr.next
            if sPtr : sPtr = sPtr.next

        if carry == 1 :
            dPtr.next = ListNode(1)
            
        return reverseNodes(dummyNode.next)
