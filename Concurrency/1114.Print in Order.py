import threading as T

class Foo:
    def __init__(self):

        self.lock = T.Lock()
        self.condition = T.Condition(self.lock)
        self.state = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:

        with self.condition :

            printFirst()
            self.state = 1

            self.condition.notify_all()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        with self.condition :

            while self.state != 1 :
                self.condition.wait()

            printSecond()
            self.state = 2

            self.condition.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        with self.condition :

            while self.state != 2 :
                self.condition.wait()
                
            printThird()
