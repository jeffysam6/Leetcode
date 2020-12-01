class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowels = ['a','e','i','o','u']
        
        s = S.split()
        
        for index,word in enumerate(s):
            if(word[0].lower() in vowels):
                s[index] = s[index]+'ma'
            
            else:
                p = s[index][0]
                s[index] = s[index][1:]
                s[index]  = s[index] + p + 'ma'
            
            
            s[index] += 'a'*(index+1)
        
        
        
        return ' '.join(s)
                