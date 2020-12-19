class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        one,two = float('inf'),float('inf')
        
        for i in nums:
            
            one = min(i,one)
            
            if(i > one):
                two = min(i,two)
                
            if(i > two):
                return True
            
        
        return False