class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = [1]
        i = 1
        
        if(n == 0):
            return 0
        
        curr = coins[0]
        
        while(curr < n):
            
            i += 1
            
            curr += i
            
            if(curr > n):
                return i - 1
            
            
            
            # print(curr,i)
        
        
        return i
            