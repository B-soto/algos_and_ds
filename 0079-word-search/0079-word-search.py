class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        word_exists = False
        rows = len(board)
        cols = len(board[0])
        
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        
        def dfs(row,col, index):
            nonlocal word_exists
            nonlocal directions
            #Base Case
            #1) Out of Bounds
            if row >= rows or row < 0 or col >= cols or col < 0:
                return
            #2) Check visited
            if board[row][col] == "!":
                return
            
            #3) Check if valid spot
            if board[row][col] != word[index]:
                return
            else:
                index +=1
            
            #4) Check if word is found
            if index == len(word):
                word_exists = True
                return 
            
            #mark Visited
            temp = board[row][col]
            board[row][col] = "!"
            
            for d in directions:
                dfs(row+d[0], col+d[1], index)
                
            
            board[row][col] = temp
            
                    
        
        
        for r in range(rows):
            for c in range(cols):
                
                dfs(r,c, 0)
        
        return word_exists
        
        