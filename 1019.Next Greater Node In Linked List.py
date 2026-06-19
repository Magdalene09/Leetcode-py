# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
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
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head = reverseNodes(head)
        result = []
        stack = []

        curPtr = head

        while curPtr :
            while stack and stack[-1] <= curPtr.val :
                stack.pop()

            if stack : result.append(stack[-1])
            else : result.append(0)

            stack.append(curPtr.val)

            curPtr = curPtr.next

        return result[::-1]
'''

def linkedListToArray(head) :
    arr = []
    curPtr = head

    while curPtr :
        arr.append(curPtr.val)
        curPtr = curPtr.next

    return arr

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = linkedListToArray(head)
        n = len(arr)
        stack = []
        result = []

        for i in range(n - 1,-1,-1) :
            while stack and stack[-1] <= arr[i] :
                stack.pop()

            if stack : result.append(stack[-1])
            else : result.append(0)

            stack.append(arr[i])

        return result[::-1]
