class Solution:
    def canConstruct(self, ransom: str, magazine: str) -> bool:
        from collections import Counter
        
        ransom = Counter(ransom)
        magazine = Counter(magazine)

        for i in ransom:

            if(ransom[i] > magazine[i]):
                return False

        return True
