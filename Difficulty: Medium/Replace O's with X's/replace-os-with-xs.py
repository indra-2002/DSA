class Solution:
    
    
    
    def fill(self, grid):
        # Code here
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c <0 or c>= len(grid[0]) or grid[r][c]!="O":
                return 
            grid[r][c]="S"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[0][j]=='O': dfs(0,j)
                if grid[len(grid)-1][j]=="O": dfs(len(grid)-1,j)
                if grid[i][0]=="O": dfs(i,0)
                if grid[i][len(grid[0])-1] =="O": dfs(i,len(grid[0])-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="S":
                    grid[i][j]= "O"
                elif grid[i][j]=="O":
                    grid[i][j]="X"
        
                    