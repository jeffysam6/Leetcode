class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        
        
        
        def recurse(nums,ans,subset,i):
            
            ans.append(list(subset))
            
            for k in range(i,len(nums)):
                
                subset.append(nums[k])
                
                recurse(nums,ans,subset,k+1)
                
                subset.pop()
                
        
        recurse(nums,ans,[],0)
        
        return ans