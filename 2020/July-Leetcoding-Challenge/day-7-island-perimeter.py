grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

ans = 0

for i in range(len(grid)):
	for j in range(len(grid[0])):

 		if(grid[i][j] == 1):

 			if( (i-1 >= 0 and grid[i-1][j] != 1) or i-1 < 0):
 				ans += 1

 			if( (i+1 < len(grid) and grid[i+1][j] != 1) or i+1>=len(grid)):
 				ans += 1


 			if( (j+1 < len(grid[0]) and grid[i][j+1] != 1) or j+1 >= len(grid[0])):
 				ans += 1

 			if( (j-1 >=0 and grid[i][j-1] != 1) or j-1<0):
 				ans += 1


print(ans)
