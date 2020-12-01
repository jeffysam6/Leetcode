class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        ans = []
        
        candidates.sort()
        
        
        def combi(curr,t):
            
            if(t == 0):
                ans.append(curr)
                return 
            
            if(t < 0):
                return
            
            
            for i in candidates:
                if(not curr or i >= curr[-1]):
                    combi(curr + [i], t - i)
        
        
        
        combi([],target)
        
        
        return(ans)
        
        
        # return ans