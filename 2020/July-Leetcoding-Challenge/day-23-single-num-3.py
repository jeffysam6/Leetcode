class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        total = 0
        
        for n in nums:
            total ^= n
            
        mask = total & -total
        
        a,b = 0,0
        for n in nums:
            
            if(mask & n):
                a ^= n
            
            else:
                b ^= n
                
        
        return [a,b]


# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
        
#         d = {}
        
#         for i in nums:
#             d[i] = d.get(i,0) + 1
        

        
#         return [i for i,j in d.items() if j == 1] 
#         