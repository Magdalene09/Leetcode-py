class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class MyLinkedList:

    def __init__(self):
        self.root=None

        

    def get(self, index: int) -> int:
        cur=self.root
        count=0
        while cur:
            if count==index:
                return cur.data
            cur=cur.next
            count+=1
        return -1
        

    def addAtHead(self, val: int) -> None:
        ll=Node(val)
        ll.next=self.root
        self.root=ll
        

    def addAtTail(self, val: int) -> None:
        ll=Node(val)
        if self.root is None:
            self.root=ll
            return
        cur=self.root
        while cur.next:
            cur=cur.next
        cur.next=ll
        

    def addAtIndex(self, index: int, val: int) -> None:
        ll=Node(val)
        if index==0:
            ll.next=self.root
            self.root=ll
            return
        cur=self.root
        count=0
        while cur and count<index-1:
            cur=cur.next
            count+=1
        if cur is None:
            return
        ll.next=cur.next
        cur.next=ll

        

    def deleteAtIndex(self, index: int) -> None:
        if self.root is None:
            return
        if index==0:
            self.root=self.root.next
            return
        cur=self.root
        count=0
        while cur.next and count<index-1:
            cur=cur.next
            count+=1
        if cur.next:
            cur.next=cur.next.next
        
