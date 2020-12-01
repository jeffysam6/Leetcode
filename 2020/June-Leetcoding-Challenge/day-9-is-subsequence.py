class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = []
        
        if(s == ''):
            return True
        
        i = 0
        
        for char in t:
            if(i<len(s) and char == s[i]):
                stack.append(char)
                i += 1
        
        if(s == ''.join(stack)):
            return True
        else:
            return False