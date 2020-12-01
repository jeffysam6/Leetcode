class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        
        c = Counter(nums)
        
        return min(c,key=c.get)
        
      