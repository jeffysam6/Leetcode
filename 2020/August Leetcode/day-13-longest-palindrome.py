class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        
        for i in s:
            d[i] = d.get(i,0) + 1
        
        max_odd = 0
        
        has_odd = False
        
        c = 0
        
        for i in d.keys():
            
            if(d[i]%2 != 0):
                has_odd = True
        
            c += d[i]//2 * 2
            

                
        # c += max_odd
        
        return c if not has_odd else c+1
