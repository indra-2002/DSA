class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        curcolor=image[sr][sc]
        if image[sr][sc]==color:
            return image
        def dfs(r,c):
            if r>=rows or c >=cols or  r<0 or  c<0 or  image[r][c]!= curcolor:
                return 
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image