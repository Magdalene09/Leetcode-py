# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        if not root: return ""
        
        serial = []
        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            
            if node:
                if not serial : serial.append(str(node.val))
                else : 
                    serial.append(',')
                    serial.append(str(node.val))

                dq.append(node.left)
                dq.append(node.right)
            
            else :
                if not serial : serial.append('#')
                else :
                    serial.append(',')
                    serial.append('#')

        return ''.join(serial)
        
    def deserialize(self, data):
        if not data: return None

        string = data.split(',')
        n = len(string)

        root = TreeNode(int(string[0]))
        dq = deque()

        dq.append(root)

        i = 1

        while dq and i < n :

            node = dq.popleft()

            node.left = TreeNode(int(string[i])) if i < n and string[i] != '#' else None
            node.right = TreeNode(int(string[i + 1])) if i + 1 < n and string[i + 1] != '#' else None

            if node.left :
                dq.append(node.left)

            if node.right :
                dq.append(node.right)

            i += 2

        return root
