import threading as T

class FizzBuzz:

    def __init__(self, n: int):
        self.n = n
        self.lock = T.Lock()
        self.condition = T.Condition(self.lock)
        self.num = 1

    def fizz(self, printFizz):

        while True:
            with self.condition:

                while self.num <= self.n and (
                    self.num % 3 != 0 or self.num % 5 == 0
                ):
                    self.condition.wait()

                if self.num > self.n:
                    self.condition.notify_all()
                    return

                printFizz()
                self.num += 1
                self.condition.notify_all()

    def buzz(self, printBuzz):

        while True:
            with self.condition:

                while self.num <= self.n and (
                    self.num % 3 == 0 or self.num % 5 != 0
                ):
                    self.condition.wait()

                if self.num > self.n:
                    self.condition.notify_all()
                    return

                printBuzz()
                self.num += 1
                self.condition.notify_all()

    def fizzbuzz(self, printFizzBuzz):

        while True:
            with self.condition:

                while self.num <= self.n and (
                    self.num % 3 != 0 or self.num % 5 != 0
                ):
                    self.condition.wait()

                if self.num > self.n:
                    self.condition.notify_all()
                    return

                printFizzBuzz()
                self.num += 1
                self.condition.notify_all()

    def number(self, printNumber):

        while True:
            with self.condition:

                while self.num <= self.n and (
                    self.num % 3 == 0 or self.num % 5 == 0
                ):
                    self.condition.wait()

                if self.num > self.n:
                    self.condition.notify_all()
                    return

                printNumber(self.num)
                self.num += 1
                self.condition.notify_all()
