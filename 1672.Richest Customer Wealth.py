class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0

        
        for bank in accounts :
            amt = 0
            for money in bank :
                amt += money
            if amt > max_sum :
                max_sum =amt

        return max_sum
