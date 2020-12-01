class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        
        if(n < 2):
            return n
        
        i = 1
        
        while(i*i <= n):
            squares.append(i*i)
            i += 1
            
        
        ans = 0
        
        check = {n}
        
        while(check):
            ans += 1
            temp = set()
            for x in check:
                
                
                for y in squares:
                    
                    if(x == y):
                        return ans
                    
                    elif(x < y):
                        break
                    
                    temp.add(x-y)
            check = temp
        
        return ans
                    
                    