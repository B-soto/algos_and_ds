class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #
        
        
        '''
         
        [[".",".",".",  ".","5",".",  ".","1","."]
        ,[".","4",".",  "3",".",".",  ".",".","."]
        ,[".",".",".",  ".",".","3",  ".",".","1"]
        
        ,["8",".",".",".",".",".",".","2","."]
        ,[".",".","2",".","7",".",".",".","."]
        ,[".","1","5",".",".",".",".",".","."]
        ,[".",".",".",".",".","2",".",".","."]
        ,[".","2",".","9",".",".",".",".","."]
        ,[".",".","4",".",".",".",".",".","."]]

        
        
        '''
        
        # runTime = O3(m*n) == (m*n)
        # space  = o(1)
        #isValid Variable O(1)
        
        isValid = True
        
        # Check rows to see if all rows are valid, (M*n)
        # if not return isValid =False
        #we Know everything is 1-9 or 0-8
        
        for i in range(9):
            seen_number_set = set()
            for j in range(9):
                value = board[i][j]
                if value != '.':
                    if value in seen_number_set:
                        return False
                    else:
                        seen_number_set.add(value)
                    
                
        
        
        # Check cols to see if all Columns are valid,  (m*n)
        # if not return isValid =False
        for i in range(9):
            seen_number_set = set()
            for j in range(9):
                value = board[j][i]
                if value != '.':
                    if value in seen_number_set:
                        return False
                    else:
                        seen_number_set.add(value)
        
        #check each 3x3 sqaure O(m*n)
        #if not reutrn isValid=False
        
        starting_points = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                starting_points.append([i,j])
        
        
        for point in starting_points:
            x,y = point
            seen_number_set = set()
            for i in range(3):
                for j in range(3):
                    value = board[i+x][j+y]
                    # print(f"({i+x},{j+y}) - {value}")
                    # print(seen_number_set)
                    if value != '.':
                        if value in seen_number_set:
                            return False
                        else:
                            seen_number_set.add(value)
                    
        
        
        #return isValid
        return isValid