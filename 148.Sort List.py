# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getMidLL(head) :
    slowPtr = head
    fastPtr = head
    fastPtr = fastPtr.next

    while fastPtr and fastPtr.next :
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr

def mergeLL(lHead,rHead) :
    dummyNode = ListNode(-1)
    temp = dummyNode

    while lHead and rHead :
        if lHead.val > rHead.val :
            temp.next = rHead    
            rHead = rHead.next

        else :
            temp.next = lHead
            lHead = lHead.next

        temp = temp.next

    if lHead : temp.next = lHead
    else : temp.next = rHead

    return dummyNode.next        

def mergeSortLL(head) :
    if not head or not head.next : return head

    middle = getMidLL(head)
    leftHead = head
    rightHead = middle.next
    middle.next = None

    leftHead = mergeSortLL(leftHead)
    rightHead = mergeSortLL(rightHead)

    return mergeLL(leftHead,rightHead)
   
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return mergeSortLL(head)
