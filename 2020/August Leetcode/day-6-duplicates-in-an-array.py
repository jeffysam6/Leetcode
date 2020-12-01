class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range(len(nums)):
            loc = nums[abs(nums[i])-1]
            
            if(loc >=0 ):
                nums[abs(nums[i])-1] = -1 * nums[abs(nums[i])-1]
            
            else:
                ans.append(abs(nums[i]))
        
        return ans
        
        
#         from collections import Counter
        
#         c = Counter()
        
#         ans = set()
        
#         for i in nums:
#             c[i] += 1
            
#             if(c[i] == 2):
#                 ans.add(i)
        
        
#         return list(ans)