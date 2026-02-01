class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_char(ch) :
            l = 0
            r = 0
            max_len = 0
            count_ch = 0

            while r < len(answerKey) :
                if answerKey[r] == ch :
                    count_ch += 1

                if count_ch > k :
                    if answerKey[l] == ch:
                        count_ch -= 1
                
                    l += 1

                max_len = max(max_len,r-l+1)
                r+= 1
            
            return max_len

        return max(max_char('F'),max_char('T'))


        
      


        

        
        
