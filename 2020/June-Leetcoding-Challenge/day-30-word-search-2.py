class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isEnd = False
        

class Trie:
    
    def __init__(self):
        self.root = Node()
        
    
    def addWord(self,word):
        curr = self.root
        for w in word:
            curr = curr.children[w]
        curr.isEnd = True
    
    def search(self,word):
        curr = self.root
        for w in word:
            curr = curr.children.get(w)
            if(not curr):
                return False
            
        return curr.isEnd
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        t = Trie()
        ans = []
        
        node = t.root
        
        for w in words:
            t.addWord(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,node,i,j,'',ans)
                
        return ans
                
    
    
    def dfs(self,board,node,i,j,chars,ans):
        
        if(node.isEnd):
            ans.append(chars)
            node.isEnd = False
        
        if(i<0 or i >= len(board) or j <0 or j >= len(board[0])):
            return
        
        char = board[i][j]
        
        node = node.children.get(char)
        
        if(not node ):
            return
        
        board[i][j] = '#'
        
        self.dfs(board,node,i+1,j,chars+char,ans)
        self.dfs(board,node,i,j+1,chars+char,ans)
        self.dfs(board,node,i-1,j,chars+char,ans)
        self.dfs(board,node,i,j-1,chars+char,ans)
        
        board[i][j] = char
            
        

        