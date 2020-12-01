class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        
                
        if(num <= 0):
            return False
        
        if(num==1 or (num & num-1 ==0 and bin(num)[2:].count('0')%2 == 0)):
            return True
        
        return False
        

#         if(num <= 0):
#             return False
        
#         while(num > 1):
            
#             if(num % 4 != 0):
#                 return False
            
#             num = num // 4
        
#         return True
    