"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def createCopyNodes(head) :
    curPtr = head

    while curPtr :
        copyNode = Node(curPtr.val)
        temp = curPtr.next
        curPtr.next = copyNode
        copyNode.next = temp

        curPtr = curPtr.next.next

def randomAllocation(head) :
    curPtr = head

    while curPtr :
        copyNode = curPtr.next
        copyNode.random = curPtr.random.next if curPtr.random else None
        curPtr = curPtr.next.next

def clonedRandomList(head) :
    if not head  : return None 
    dummyNode = Node(-1)
    dPtr = dummyNode
    curPtr = head

    while curPtr :
        dPtr.next = curPtr.next
        dPtr = dPtr.next
        curPtr.next = curPtr.next.next

        curPtr = curPtr.next

    return dummyNode.next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        createCopyNodes(head)
        randomAllocation(head)
        return clonedRandomList(head)
