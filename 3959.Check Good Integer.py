def digitSum(num):
    totalSum = 0

    while num > 0:
        totalSum += num % 10
        num //= 10

    return totalSum

def squareSum(num):
    totalSum = 0

    while num > 0:
        totalSum += (num % 10) ** 2
        num //= 10

    return totalSum

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digSum = digitSum(n)
        sqSum = squareSum(n)

        return sqSum - digSum >= 50
