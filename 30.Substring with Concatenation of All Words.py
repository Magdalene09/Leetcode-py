class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        reqMap = {}
        result = []

        for word in words:
            reqMap[word] = reqMap.get(word, 0) + 1

        n = len(s)
        m = len(words)
        x = len(words[0])
        
        for start in range(x):
            hmap = {}
            formed = 0
            left = start

            for right in range(start, n - x + 1, x):
                word = s[right : right + x]

                if word not in reqMap:
                    hmap = {}
                    formed = 0
                    left = right + x
                    continue

                hmap[word] = hmap.get(word, 0) + 1
                formed += 1

                while hmap[word] > reqMap[word]:
                    elm = s[left : left + x]
                    hmap[elm] -= 1

                    if hmap[elm] == 0 : del hmap[elm]
                    formed -= 1
                    left += x

                if formed == m : result.append(left)      

        return result
