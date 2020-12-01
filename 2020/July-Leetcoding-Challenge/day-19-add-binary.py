class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = list(a)
        b = list(b)
        
        c = 0
        ans = ''
        while(a or b or c):
            
            
            if(a):
                c += int(a.pop())
                
            if(b):
                c += int(b.pop())
                
            
            ans = str(c%2) + ans
            
            c = c//2
        
        return ans