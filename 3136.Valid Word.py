class Solution:
    def isValid(self, word: str) -> bool:
        vow ='aeiou'
        vow += vow.upper()
        consonants='qwrtypsdfghjklzxcvbnm'
        consonants += consonants.upper()
        allowed = vow + consonants + '0123456789'

        if len(word) < 3:return False
        has_vow = False
        has_con = False
        for char in word :
            if char in vow : has_vow = True
            if char in consonants : has_con = True
            if char not in allowed : return False
        return has_vow and has_con
