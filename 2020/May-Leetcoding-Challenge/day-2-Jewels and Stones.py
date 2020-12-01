class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sett = set(J)
        
        c = 0
        
        for i in S:
            if(i in sett):
                c += 1
                
        
        return c