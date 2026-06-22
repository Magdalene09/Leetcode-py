"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

def childTail(head) :
    curPtr = head
    tail = head

    while curPtr : 
        if curPtr.child :
            nextNode = curPtr.next
            _tail = childTail(curPtr.child)

            curPtr.next = curPtr.child
            curPtr.child.prev = curPtr
            curPtr.child = None

            if nextNode :
                _tail.next = nextNode
                nextNode.prev = _tail

            curPtr = _tail
        
        tail = curPtr
        curPtr = curPtr.next
    
    return tail

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return head
        childTail(head)
        return head
