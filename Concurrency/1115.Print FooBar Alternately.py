import threading as T

class FooBar:
    def __init__(self, n):

        self.n = n
        self.lock = T.Lock()
        self.condition = T.Condition(self.lock)
        self.turn = 0


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            with self.condition :
                while self.turn != 0 :
                    self.condition.wait()
                    
                printFoo()
                self.turn = 1
                self.condition.notify_all()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):

            with self.condition :
                while self.turn != 1 :
                    self.condition.wait()
                    
                printBar()
                self.turn = 0
                self.condition.notify_all()
