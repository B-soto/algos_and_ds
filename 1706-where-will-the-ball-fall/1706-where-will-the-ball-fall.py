class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        rows = len(grid)
        cols = len(grid[0])
        cache = {}
        
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            if c < 0 or c >=cols:
                return -1
            if r == rows:
                return c
            if grid[r][c] == 1:
                if c+1 < cols and grid[r][c+1] == -1:
                    return -1
                else:
                    ans = dfs(r+1, c+1)
                    cache[(r,c)] = ans
                    return ans
            else:
                if c-1 >= 0 and grid[r][c-1] == 1:
                    return -1
                else:
                    ans = dfs(r+1,c-1)
                    cache[(r,c)] = ans
                    return ans
                
        return [dfs(0,i) for i in range(cols)]
                    
                
            
        