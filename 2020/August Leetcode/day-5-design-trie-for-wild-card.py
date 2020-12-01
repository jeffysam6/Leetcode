class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for w in word:
            if(w  in curr.children):
                curr = curr.children[w]
            else:
                curr.children[w] = TrieNode()
                curr = curr.children[w]
                
        curr.isWord = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        self.ans = False
        
        self.dfs(curr,word)
        
        return self.ans
    
    def dfs(self,curr,word):
        
        if(not word):
            if(curr.isWord):
                self.ans = True
            return
        
        if(word[0] == '.'):
            
            for n in curr.children.values():
                self.dfs(n,word[1:])
        
        else:
            if(word[0] in curr.children):
                curr = curr.children[word[0]]
                self.dfs(curr,word[1:])
            else:
                return
#         for index,w in enumerate(word):
            
#             if(w is '.'):
#                 return self.search(word[index+1:])
            
#             if(w  in curr.children):
#                 curr = curr.children[w]
#             else:
#                 return False
        
#         return True
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)