class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        nums = [0,1]
        max_element = 1

        for i in range(2,n+1) :
            if i % 2 == 0 :
                val = nums[i//2]
                nums.append(val)
                if val > max_element :
                    max_element = val
            else :
                t = i//2
                val = nums[t]  + nums[t+1]
                nums.append(val)
                if val > max_element :
                    max_element = val
        
        return max_element
