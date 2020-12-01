class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        ans = ''
        
        N = (bin(N))
        
        # print(N)
        
        for i in range(2,len(N)):
            
            ans += str(int(N[i]) ^ 1)
            # print(int(N[i]) ^ 1)
        
        return(int(ans,2))