class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        cache = {}
        
        def dfs(row,col):
            #base case
            key = f"{row}_{col}"
            if key in cache:
                return cache[key]
            if row >= rows or row < 0 or col >= cols or col < 0:
                return 0
            if grid[row][col] == 1:
                return 0
            if (row,col) == (rows-1, cols-1):
                return 1
            
            #go down
            down_paths = dfs(row+1,col)
            
            #go right
            left_paths = dfs(row,col+1)
            
            cache[key] = down_paths + left_paths
            
            return down_paths + left_paths
        
        
        total_paths = dfs(0,0)
        return total_paths
        