"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
def dfs(node) :
    
    if not node : return
    cur = node

    while cur.left :
        temp = cur

        while temp :
            
            temp.left.next = temp.right
            
            if temp.next :
                right = temp.right
                temp = temp.next
                right.next = temp.left

            else : break
        
        cur = cur.left

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root : return root
        dfs(root)

        return root
