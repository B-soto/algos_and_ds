class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Given our input Grid, we should. be able to initalize a returnGrid
        # len(grid) - 2 x len(grid-2), initalize them all to 0
        
        rows = len(grid)
        cols = len(grid)
        rtn_grid = [[0 for x in range(rows-2)] for y in range(cols-2)]
        
        # Create starting points and from each starting point, 
        #Iterate over starting points - we do a check in a 3x3 square 
        #Keep track of max 
        #after we finish each starting point, update max at that starting point
        # start_points 
        for r in range(len(rtn_grid)):
            for c in range(len(rtn_grid)):
                curr_max = 0
                for i in range(3):
                    for j in range(3):
                        val = grid[i+r][j+c]
                        curr_max = max(curr_max, val)
                rtn_grid[r][c] = curr_max
                
        return rtn_grid
            
            

        
                
            
            
                
        
        
                
                
        
        