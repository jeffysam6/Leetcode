class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if(word == word[0].upper() + word[1:].lower() or
            word == word.lower() or word == word.upper()):
            return True
        
        return False