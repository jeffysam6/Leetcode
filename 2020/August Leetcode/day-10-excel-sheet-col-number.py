class Solution:
    def titleToNumber(self, s: str) -> int:
        
        l = len(s) - 1

        index = 0

        column = 0
        while(index<len(s)):

            column += (26**l) *(ord(s[index])-64)
            index += 1
            l -= 1

        return(column)
