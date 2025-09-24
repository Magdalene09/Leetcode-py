class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        X=[]
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                X.append("FizzBuzz")
            elif i % 3 == 0:
                X.append("Fizz")
            elif i % 5 == 0:
                X.append("Buzz")
            else:
                X.append(str(i))
        return X
