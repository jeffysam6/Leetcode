class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = list(bin(n)[2:])
        
        len_n = len(n)
        
        diff = 32 - len_n
        
        n = ['0']*diff + n
        
        
        l = 0
        r = len(n) - 1
        
        while(l < r):
            print(l,r)
            n[l],n[r] = n[r],n[l]
            
            l += 1
            r -= 1
            
        return(int(''.join(n),2))
