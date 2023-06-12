class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
#         total_greatest = 0 += 4 +=3 +=1
        
#         max_grid = 0
#         max_row = 0
#         temp = [[1,2]
#                 [3,1]]
        
#         curr = [[1,2,4]
#                 [3,3,1]]
        
        #Create a current_grid, temp_grid, curr_row_max, curr_grid_max
        
        curr = grid
        total = 0
        
        while curr:
            # print(curr)
            temp = []
            curr_grid_max = None
            
            rows, cols = len(curr), len(curr[0])
            
            #find each rows and grids max
            for r in range(rows):
                curr_row_max = None
                #find max
                for c in range(cols):
                    if curr_row_max is None:
                        curr_row_max = c
                    if curr[r][c] > curr[r][curr_row_max]:
                        curr_row_max = c
                    # curr_row_max = max(curr[r][c], curr[r][curr_row_max])
                
                #add in all values except curr_row_max
                new_col = []
                for c in range(cols):
                    if c != curr_row_max:
                        new_col.append(curr[r][c])
                temp.append(new_col)
                    
                #update curr_grid_max after every row
                if curr_grid_max is None:
                    curr_grid_max = [r,curr_row_max]
                
                if curr[r][curr_row_max] > curr[curr_grid_max[0]][curr_grid_max[1]]:
                        curr_grid_max = [r,curr_row_max]
                # else:
                #     curr_grid_max = max(curr[curr_grid_max[0]][curr_grid_max[1]], curr[r][curr_row_max])
            #update total
            total += curr[curr_grid_max[0]][curr_grid_max[1]]
            if temp[0] == []:
                break
            
            curr = temp
            
        return total
                
                                       
            
            
        
        
        