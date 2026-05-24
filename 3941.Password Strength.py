class Solution:
    def passwordStrength(self, password: str) -> int:
        n = len(password)
        strength = 0
        seen = [False] * 128

        for i in range(n) :
            charVal = ord(password[i])

            if not seen[charVal] :
                if ord('a') <= charVal <= ord('z') : strength += 1
                elif ord('A') <= charVal <= ord('Z') : strength += 2
                elif ord('0') <= charVal <= ord('9') : strength += 3
                else : strength += 5

                seen[charVal] = True
                
        return strength
