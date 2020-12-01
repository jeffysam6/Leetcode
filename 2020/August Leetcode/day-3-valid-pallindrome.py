class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered = ''
        
        s = s.lower()
        
        for i in s:
            if(ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9')):
                filtered += i
        
        
        l = 0
        r = len(filtered) - 1
        
        
        
        while(l < r):
            
            if(filtered[l] != filtered[r]):
                return False
            
            l += 1
            r -= 1
            
        return True