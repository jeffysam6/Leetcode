class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        i = len(digits) - 1
        
        while(i >= 0):
            carry = False
            
            digits[i] += 1
            
            if(digits[i] > 9):
                carry = True
                digits[i] = 0
            
            if(carry == False):
                break
            
            i -= 1
            
            if(i == -1 and carry):
                digits[0] = 0
                return [1] + digits
        
        
        return digits
                
        
        