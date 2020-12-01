class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        return n>0 and bin(n)[2:].count('1') == 1