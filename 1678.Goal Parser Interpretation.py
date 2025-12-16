class Solution:
    def interpret(self, command: str) -> str:
        word = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                word += "G"
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                word += "o"
                i += 2
            else :
                word += "al"
                i += 4
        return word
            

