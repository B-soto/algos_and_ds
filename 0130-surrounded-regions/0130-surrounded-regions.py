from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # iterate the border of the board
        # Run a BFS on all cells with a 0. Every cell we touch on the border from our bfs we will put in a visited set
        # Iterate over the board and turn everything to a x that is not in our visted_set
        
        q = deque()
        
        #top & Bottom Row 
        for i in range(len(board[0])):
            # print((0,i), (len(board))-1,i)
            if board[0][i] == 'O':
                q.append([0,i])
            
            if board[len(board)-1][i] == 'O':
                q.append([len(board)-1,i])
                
        #left and right columns
        for i in range(len(board)):
            # print((i,0), (len(board[0])-1,0))
            if board[i][0] == 'O':
                q.append([i,0])
                
            if board[i][len(board[0])-1] == 'O':
                q.append([i,len(board[0])-1])
                  
        print(q)
        
        # Do a BFS on all in the q:
        visited = set()
        
        while q:
            r,c = q.popleft()
            if (r,c) in visited:
                continue
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                continue
            if board[r][c] == 'X':
                continue
                
            visited.add((r,c))
            q.append((r+1,c))
            q.append((r-1,c))
            q.append((r,c+1))
            q.append((r,c-1))
                
        print(visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(i,j)
                if (i,j) not in visited:
                    board[i][j] = 'X'
                
                
        
        