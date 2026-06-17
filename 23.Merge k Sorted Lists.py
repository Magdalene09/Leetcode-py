# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as h

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i , node in enumerate(lists) :
            if node : h.heappush(pq,[node.val,i,node])

        dummyNode = ListNode(-1)
        dPtr = dummyNode

        while pq :
            minNode = h.heappop(pq)
            dPtr.next = minNode[2]
            if minNode[2].next : h.heappush(pq,[minNode[2].next.val,minNode[1],minNode[2].next])
            dPtr = dPtr.next

        return dummyNode.next
