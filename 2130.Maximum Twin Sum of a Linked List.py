# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def findMiddleNode(head) :
    slowPtr = head
    fastPtr = head

    while fastPtr and fastPtr.next :
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr

def reverseNodes(head) :
    prev = None
    curPtr = head

    while curPtr :
        temp = curPtr.next
        curPtr.next = prev
        prev = curPtr
        curPtr = temp

    return prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head : return 0
        if not head.next : return head.val

        maxSum = 0
        middleNode = findMiddleNode(head)
        reverseHead = reverseNodes(middleNode)

        firstPtr = head
        secondPtr = reverseHead

        while secondPtr :
            maxSum = max(firstPtr.val + secondPtr.val, maxSum)
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        return maxSum
