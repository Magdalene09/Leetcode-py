# Approach 1 (Semaphores)
import threading

class DiningPhilosophers:
    def __init__(self):
        
        self.semaphore = threading.Semaphore(4)
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self, philosopher: int, 
                   pickLeftFork: 'Callable[[], None]', 
                   pickRightFork: 'Callable[[], None]', 
                   eat: 'Callable[[], None]', 
                   putLeftFork: 'Callable[[], None]', 
                   putRightFork: 'Callable[[], None]') -> None:
        
        
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        
        with self.semaphore:
            
            with self.forks[left_fork]:
                with self.forks[right_fork]:
                    
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putLeftFork()
                    putRightFork()

# Approach 2 (Conditional Variables)
import threading as T

class DiningPhilosophers:

    def __init__(self):
        self.lock = T.Lock()
        self.condition = T.Condition(self.lock)
        self.forks = [True] * 5

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork,
        pickRightFork,
        eat,
        putLeftFork,
        putRightFork
    ) -> None:

        leftFork = philosopher
        rightFork = (philosopher + 1) % 5

        with self.condition:

            while not (
                self.forks[leftFork]
                and self.forks[rightFork]
            ):
                self.condition.wait()

            self.forks[leftFork] = False
            self.forks[rightFork] = False

        pickLeftFork()
        pickRightFork()

        eat()

        putLeftFork()
        putRightFork()

        with self.condition:
            
            self.forks[leftFork] = True
            self.forks[rightFork] = True

            self.condition.notify_all()
