class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        asteroids.sort()
        for i in range(n) :
            if mass < asteroids[i] :
                return False

            mass += asteroids[i]

        return True
