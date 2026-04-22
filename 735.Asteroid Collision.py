class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        result = []

        for i in range(n):
            if asteroids[i] > 0 :
                result.append(asteroids[i])

            else :
                while result and result[-1] > 0 and result[-1] < abs(asteroids[i]) :
                    result.pop()

                if result and result[-1] == abs(asteroids[i]) :
                    result.pop()

                elif not result or result[-1] < 0 :
                    result.append(asteroids[i])


        return result
