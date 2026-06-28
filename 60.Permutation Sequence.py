class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = []
        fact = 1

        for i in range(1,n) :
            nums.append(i)
            fact = fact * i

        nums.append(n)
        k = k - 1

        kThSequence = ""

        while True :

            kThSequence += str(nums[k // fact])
            nums.pop(k // fact)

            if not nums : break

            k = k % fact
            fact //= len(nums)

        return kThSequence
