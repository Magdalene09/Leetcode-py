class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen_letters = []
        for letters in s :
            if letters in seen_letters :
                return letters
            else :
                seen_letters.append(letters)
        
