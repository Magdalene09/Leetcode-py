class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        result = []
        p_count = Counter(p)
        window = Counter()

        for right in range(len(s)):
            window[s[right]] += 1

            if right - left + 1 > len(p) :
                window[s[left]] -= 1
                if window[s[left]] == 0 :
                    del window[s[left]]
                
                left += 1
            
            if window == p_count :
                result.append(left)
        
        return result


        
