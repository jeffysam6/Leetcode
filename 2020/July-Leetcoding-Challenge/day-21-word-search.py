
class Solution:
    
    def dfs(self,i,j,word,board):
        
        if(len(word) == 0):
            return True
        
        if(i<0 or j<0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]):
            return False
        
        val = board[i][j] 
        
        board[i][j] = '#'
        
        found = self.dfs(i+1,j,word[1:],board) or self.dfs(i-1,j,word[1:],board) or             self.dfs(i,j+1,word[1:],board) or self.dfs(i,j-1,word[1:],board)
        
        board[i][j] = val
        
        return found
        
        
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if(self.dfs(i,j,word,board)):
                    return True
        
        return False
                    
                