class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newnode=ListNode(0)
        newnode.next=head
        cur=newnode
        while cur.next :
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        
        return newnode.next
