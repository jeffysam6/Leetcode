class Solution:
    def findComplement(self, num: int) -> int:
        
        s = bin(num)[2:]
        
        out = ""
        
        for i in s:
            if(i == '1'):
                out += '0'
            
            else:
                out += '1'
        
        
        return int(out,2)