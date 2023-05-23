class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c):
            if c < 0 or c >=cols:
                return -1
            if r == rows:
                return c
            if grid[r][c] == 1:
                if c+1 < cols and grid[r][c+1] == -1:
                    return -1
                else:
                    return dfs(r+1, c+1)
            else:
                if c-1 >= 0 and grid[r][c-1] == 1:
                    return -1
                else:
                    return dfs(r+1,c-1)
                
        return [dfs(0,i) for i in range(cols)]
                    
                
            
        