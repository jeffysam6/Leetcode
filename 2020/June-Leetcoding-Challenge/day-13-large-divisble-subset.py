class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        subsets = {-1 : set()}
        
        for n in sorted(nums):
            temp = []
            for s in subsets:
                
                if(n % s == 0):
                    temp.append(subsets[s])
            
            subsets[n] = max(temp,key=len) | {n}
        
        
        return list(max(subsets.values(),key=len))