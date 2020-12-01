class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        stack = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if(( i==0 or  j==0 or i==len(board)-1 or j == len(board[0]) - 1) and board[i][j] == 'O'):
                    stack.append((i,j))
        
        while(stack):
            
            i,j = stack.pop(0)
            
            board[i][j] = 'T'
            
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                
                xx = i+ x
                yy = j + y
                
                if(0<xx<len(board) and 0<yy<len(board[0]) and board[xx][yy] == 'O'):
                    stack.append((xx,yy))
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 'O'):
                    board[i][j] = 'X'
                
                elif(board[i][j] == 'T'):
                    board[i][j] = 'O'
                    
        
        return board
                    
                    