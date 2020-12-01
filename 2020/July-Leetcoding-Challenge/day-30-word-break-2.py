# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def addWord(self,word):
#         curr = self.root
        
#         for w in word:
#             if(w in curr.children):
#                 curr = curr.children[w]
            
#             else:
#                 curr.children[w] = TrieNode()
#                 curr = curr.children[w]
#         curr.isWord = True
            
        
        
#     def isprefix(self,word):
#         curr = self.root
#         for w in word:
#             if(w in curr.children):
#                 curr = curr.children[w]
#             else:
#                 return False
        
#         return True
    
#     def isFullWord(self,word):
#         curr = self.root
#         for w in word:
#             if(w in curr.children):
#                 curr = curr.children[w]
#             else:
#                 return False
        
#         if(curr.isWord):
#             return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        return self.dfs(s,wordDict,{})


            
            
        
    def dfs(self,s,wordDict,memo):
        
        if(s in memo):
            return memo[s]
        
        if(not s):
            return []


        res = []
        for word in wordDict:

            if(not s.startswith(word)):
                continue

            if(len(word) == len(s)):
                res.append(word)

            else:
                processRest = self.dfs(s[len(word):],wordDict,memo)
                for item in processRest:
                    item = word + ' ' + item
                    res.append(item)
            
        memo[s] = res
        
        return res
            
#         ans = []
        
#         # print(trie.isprefix('ca'))
        
#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
                
#                 if(trie.isprefix(s[i:j])):
                    
#                     if(trie.isFullWord(s[i:j])):
#                         ans.append(s[i:j])
                    
                
#                 else:
#                     break
        
#         print(ans)

            
            
        