class DLLNode :

    def __init__(self,key,val) :

        self.key = key
        self.val = val
        self.next = None
        self.prev = None

def deleteNode(Node) :

    nextNode = Node.next
    prev = Node.prev

    prev.next = nextNode
    nextNode.prev = prev

def insertAfterHead(head,Node) :

    cPtr = head
    temp = cPtr.next

    cPtr.next = Node
    Node.prev = cPtr

    Node.next = temp
    temp.prev = Node

class LRUCache:

    def __init__(self, capacity: int):

        self.hmap = {}
        self.head = DLLNode(-1,-1)
        self.tail = DLLNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self.hmap : return -1
        Node = self.hmap[key]

        deleteNode(Node)
        insertAfterHead(self.head,Node)

        return Node.val

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0 : return

        if key in self.hmap :
            Node = self.hmap[key]
            Node.val = value

            deleteNode(Node)
            insertAfterHead(self.head,Node)

        else :
            if len(self.hmap) == self.capacity :
                Node = self.hmap[self.tail.prev.key]
                del self.hmap[self.tail.prev.key]
                deleteNode(Node)

            Node = DLLNode(key,value)
            self.hmap[key] = Node
            insertAfterHead(self.head,Node)
