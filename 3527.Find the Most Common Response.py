class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        hmap = {}
        max_count = 0
        word = ""
        

        for i in range(len(responses)):
            a = set(responses[i])
            for j in a:
                hmap[j] = hmap.get(j,0) + 1
                if hmap[j] > max_count :
                    max_count = hmap[j]
                    word = j
                
                elif hmap[j] == max_count :
                    if word > j :
                        word = j

        return word

        

        

               
