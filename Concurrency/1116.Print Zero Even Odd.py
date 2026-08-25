import threading as T

class ZeroEvenOdd:

    def __init__(self, n):
        self.n = n
        self.count = 1
        
        self.zero_sem = T.Semaphore(1)
        self.even_sem = T.Semaphore(0)
        self.odd_sem = T.Semaphore(0)

    def zero(self, printNumber):
        
        while self.count <= self.n:
            self.zero_sem.acquire()
            
            if self.count > self.n:
                
                self.even_sem.release()
                self.odd_sem.release()
                break
                
            printNumber(0)
            
            if self.count % 2 == 0:
                self.even_sem.release()
            else:
                self.odd_sem.release()

    def even(self, printNumber):
        
        while self.count <= self.n:
            self.even_sem.acquire()
            
            if self.count > self.n:
                
                self.zero_sem.release()
                self.odd_sem.release()
                break
                
            printNumber(self.count)
            
            self.count += 1
            self.zero_sem.release()

    def odd(self, printNumber):
        
        while self.count <= self.n:
            self.odd_sem.acquire()
            
            if self.count > self.n:
                
                self.zero_sem.release()
                self.even_sem.release()
                break
                
            printNumber(self.count)
            
            self.count += 1
            self.zero_sem.release()
