# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def findKthNode(head,k) :
    curPtr = head
    for _ in range(k - 1) :
        if not curPtr : return None
        curPtr = curPtr.next

    return curPtr

def kGroupReverse(head,k) :
    curPtr = head
    prev = None

    for _ in range(k):
        temp = curPtr.next
        curPtr.next = prev
        prev = curPtr
        curPtr = temp

    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curPtr = head
        prevNode = None
        nextNode = None 

        while curPtr :
            kthNode = findKthNode(curPtr,k)
            
            if not kthNode :
                if prevNode : prevNode.next = curPtr
                break

            nextNode = kthNode.next
            kthNode.next = None

            kGroupReverse(curPtr,k)
            if curPtr == head : head = kthNode
            else : prevNode.next = kthNode

            prevNode = curPtr
            curPtr = nextNode

        return head
