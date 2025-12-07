class Solution:
    def ratInMaze(self, maze):
        # code here
        visited=set()
        n=len(maze)
        letter=[]
        ans=[]
        def dfs(row,col):
            if row==col==n-1:
                ans.append("".join(letter))
                return 
            
            if row<0 or row>=n or col<0 or col>=n or maze[row][col]==0 or (row,col) in visited:
                return 
            visited.add((row,col))
            letter.append("D")
            dfs(row+1,col)
            letter.pop()
            
            letter.append("U")
            dfs(row-1,col)
            letter.pop()
            
            letter.append("R")
            dfs(row,col+1)
            letter.pop()
            
            letter.append("L")
            dfs(row,col-1)
            letter.pop()
            visited.remove((row,col))
            
        dfs(0,0)
        return sorted(ans)
            
        
        
        