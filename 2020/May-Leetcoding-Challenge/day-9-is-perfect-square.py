class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        

        sqr = num** (1/2)
        
        return sqr%1==0