class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        
        rotten = deque()
        
        minutes = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(grid[i][j] == 2):
                    rotten.append([i,j])
                
                elif(grid[i][j] == 1):
                    fresh += 1
                    
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        if(fresh == 0):
            return 0
        
        if(len(rotten) == 0):
            return -1
        
        while(rotten and fresh > 0):
            
            minutes += 1
            
            for _ in range(len(rotten)):
                
                x,y = rotten.popleft()
                
                for i,j in directions:
                    
                    new_x,new_y = x+i,y+j
                    
                    if(0<=new_x <len(grid) and 0<=new_y < len(grid[0]) and grid[new_x][new_y] == 1):
                        grid[new_x][new_y] = 2
                        fresh -= 1
                        
                        rotten.append([new_x,new_y])
                        
        if(fresh > 0):
            return -1
        return minutes
                
                