class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        p_len = len(p)
        ans = []
        
        p_count = Counter(p)
        s_count = Counter(s[:p_len])
        
        j = len(p)
        i = 0
        while(j <= len(s)):
            
            if(p_count == s_count):
                ans.append(i)
                
            s_count[s[i]] -= 1
            
            if(s_count[s[i]] == 0):
                s_count.pop(s[i])
            
            if(j < len(s)):
                s_count[s[j]] += 1
                
                
            i += 1
            j += 1
            
        
    
        
        
        return ans
            