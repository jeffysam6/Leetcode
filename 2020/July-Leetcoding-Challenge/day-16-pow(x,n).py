class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n < 0):
            x = 1/x
            n = -n
        
        power = 1
        while(n):
            
            if(n % 2):
                print('odd',n,x,power)
                power = power * x
                n -= 1
                
            else:
                print('even',n,x,power)
                x =  x * x
                n = n //2
        print('out',n,x,power)
        return power