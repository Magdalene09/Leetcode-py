import threading as T

class H2O:
    def __init__(self):
        
        self.H = T.Semaphore(2)
        self.O = T.Semaphore(0)
        self.lock = T.Lock()
        self.count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        self.H.acquire()
        releaseHydrogen()

        with self.lock : 
            self.count += 1

            if self.count == 2 :
                self.O.release()
                return

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        self.O.acquire()
        releaseOxygen()

        with self.lock : self.count = 0

        self.H.release()
        self.H.release()
