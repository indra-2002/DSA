class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        visited=set()
        def dfs(row,col,index):
            
            if index == len(word):
                return True
            if row<0 or col<0 or row>=n or col>=m or board[row][col]!=word[index] or (row,col) in visited :
                return False
            visited.add((row,col))
            res=(dfs(row+1,col,index+1) or dfs(row-1,col,index+1)or dfs(row,col+1,index+1) or dfs(row,col-1,index+1))
            visited.remove((row,col))
            return res
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False