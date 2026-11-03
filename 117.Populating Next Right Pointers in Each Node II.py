"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node :
    
    def __init__(self, val) :
        self.val = val
        self.next = None

def lvlConnect(root) :

    cur = root
    while cur :

        dummy = Node(0)
        last_node = dummy

        while cur :

            if cur.left :
                last_node.next = cur.left
                last_node = cur.left

            if cur.right :
                last_node.next = cur.right
                last_node = cur.right
            
            cur = cur.next

        cur = dummy.next
        
    return root
        
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root: return root
        
        return lvlConnect(root)
