class Solution:
    def minDistance(self, word1: str, word2: str) -> int:



        grid = [ [0]*(len(word2)+1) for _ in range(len(word1)+1)]


        for i in range(len(grid)):
            grid[i][0] = i

        for i in range(len(grid[0])):
            grid[0][i] = i


        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):

                if(word2[j-1] == word1[i-1]):
                    grid[i][j] = grid[i-1][j-1] 

                else:
                    grid[i][j] = 1 + min(grid[i-1][j-1],grid[i-1][j],grid[i][j-1])

        return(grid[-1][-1])