class DLLNode :

    def __init__(self, key, val) :

        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1

class DLL :

    def __init__(self) :

        self.size = 0

        self.head = DLLNode(-1,-1)
        self.tail = DLLNode(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, Node) :

        prevNode = Node.prev
        nextNode = Node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        self.size -= 1

    def insertAfterHead(self, Node) :

        temp = self.head.next
        self.head.next = Node
        Node.prev = self.head

        Node.next = temp
        temp.prev = Node

        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
 
        self.minFreq = 0
        self.capacity = capacity

        self.nodeMap = {}
        self.freqMap = {}

    def updateFrequency(self, Node) :

        oldFreq = Node.freq
        oldList = self.freqMap[Node.freq]

        oldList.deleteNode(Node)

        if oldFreq == self.minFreq and oldList.size == 0 :
            self.minFreq += 1

        Node.freq += 1

        if Node.freq not in self.freqMap :
            self.freqMap[Node.freq] = DLL()

        self.freqMap[Node.freq].insertAfterHead(Node)

    def get(self, key: int) -> int:

        if key in self.nodeMap :
            Node = self.nodeMap[key]
            self.updateFrequency(Node)

            return Node.val

        return -1

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0 : return

        if key in self.nodeMap : 
            Node = self.nodeMap[key]
            Node.val = value
            self.updateFrequency(Node)

            return

        else :
            if len(self.nodeMap) == self.capacity:
                minFreqList = self.freqMap[self.minFreq]
                Node = minFreqList.tail.prev
                minFreqList.deleteNode(Node)
                del self.nodeMap[Node.key]

            newNode = DLLNode(key, value)
            self.nodeMap[key] = newNode

            if newNode.freq not in self.freqMap:
                self.freqMap[newNode.freq] = DLL()

            self.freqMap[newNode.freq].insertAfterHead(newNode)

            self.minFreq = 1
