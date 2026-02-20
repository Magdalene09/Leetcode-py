class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        word = []

        for ch in s :
            hmap[ch] = hmap.get(ch,0) + 1

        sorted_chars = sorted(hmap.items(),key = lambda x : x[1],reverse = True)

        for char , freq in sorted_chars :
            word.append(char*freq)

        return "".join(word)


        

        
        
