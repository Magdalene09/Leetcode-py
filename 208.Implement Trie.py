class Tnode:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:

    def __init__(self):
        self.root=Tnode()

        

    def insert(self, word: str) -> None:
        cur=self.root
        for letter in word:
            if letter not in cur.child:
                cur.child[letter]=Tnode()
            cur=cur.child[letter]
        cur.end=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for letter in word:
            if letter not in cur.child:
                return False
            cur=cur.child[letter]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for letter in prefix:
            if letter not in cur.child:
                return False
            cur=cur.child[letter]
        return True
        

