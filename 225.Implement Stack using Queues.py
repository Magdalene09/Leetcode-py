from collections import deque
class MyStack:

    def __init__(self):
        self.st=deque()
        

    def push(self, x: int) -> None:
        self.st.append(x)
        for _ in range(len(self.st)-1):
            self.st.append(self.st.popleft())
  
        

    def pop(self) -> int:
        if self.empty():
            return None
        return self.st.popleft()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.st[0]

#or
class MyStack:

    def __init__(self):
        self.st=[]
        

    def push(self, x: int) -> None:
        self.st.append(x)
  
        

    def pop(self) -> int:
        if self.empty():
            return None
        return self.st.pop()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.st[-1]
        

    def empty(self) -> bool:
        return len(self.st)==0
        


class MyStack:

    def __init__(self):
        self.st=[]
        

    def push(self, x: int) -> None:
        self.st.append(x)
  
        

    def pop(self) -> int:
        if self.empty():
            return None
        return self.st.pop()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.st[-1]
        

    def empty(self) -> bool:
        return len(self.st)==0
        
#or
class MyStack:

    def __init__(self):
        self.st=[]
        

    def push(self, x: int) -> None:
        self.st.append(x)
  
        

    def pop(self) -> int:
        if self.empty():
            return None
        return self.st.pop()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.st[-1]
        

    def empty(self) -> bool:
        return len(self.st)==0
        
