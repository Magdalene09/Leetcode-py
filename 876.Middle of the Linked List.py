class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        mid=count//2
        cur=head
        for _ in range(mid):
            cur=cur.next
        
        return cur 
