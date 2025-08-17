class MyQueue:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None

        return self.q.pop(0)
        

    def peek(self) -> int:
        if self.empty():
            return None
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q)==0
  #or
  from collections import deque
class MyQueue:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None

        return self.q.popleft()
        

    def peek(self) -> int:
        if self.empty():
            return None
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q)==0
