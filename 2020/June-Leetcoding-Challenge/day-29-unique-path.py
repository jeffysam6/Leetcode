class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[None for _ in range(n)] for _ in range(m)]


        grid[0][0] = 1

        for i in range(m):
            for j in range(n):

                if(i == 0):
                    grid[0][j] = 1

                elif(j == 0):
                    grid[i][0] = 1

                else:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]

        return(grid[-1][-1])