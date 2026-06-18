# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def findPrevMiddle(head) :
    slowPtr = head
    fastPtr = head.next

    while fastPtr and fastPtr.next :
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr

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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next : return head
        prevMiddle = findPrevMiddle(head)
        middleHead = reverseNodes(prevMiddle.next)
        prevMiddle.next = None

        curPtr = head
        mPtr = middleHead 

        while curPtr and mPtr :
            temp1 = curPtr.next
            temp2 = mPtr.next

            curPtr.next = mPtr
            mPtr.next = temp1

            curPtr = temp1
            mPtr = temp2

        if mPtr : curPtr.next = mPtr
