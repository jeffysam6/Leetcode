class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        from collections import Counter
        
        count = Counter(s)
        
        for i in range(len(s)):
            
            if(count[s[i]] == 1 ):
                return i
        
        return -1
            