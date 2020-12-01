class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        ans = 0
        for i,n in enumerate(citations):
            ans = max(min(len(citations) - i,n),ans)
            
        return ans