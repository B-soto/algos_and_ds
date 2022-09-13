class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #set a permieter_count at 0
        #Iterate over matrix until we see a 1
        #Once we find land or '1' do a DFS. Everytime we encounter water, 0 on a edge, we add 1 to count.
        #Since we know there is only one island, once our DFS is over, return the count. 
        # permieter_count = 0
        
        
        def dfs(x,y):
            def check_borders(x,y):
                count = 0
                neighbors= [(0,1),(0,-1),(-1,0),(1,0)]
                for x1,y1 in neighbors:
                    x_final = x + x1
                    y_final = y+ y1

                    if x_final < 0 or y_final < 0 or x_final > len(grid)-1 or y_final > len(grid[0])-1:
                        count +=1
                    elif grid[x_final][y_final] == 0:
                        count +=1
                    else:
                        pass
                return count 
            permieter_count = 0
            
            stack = []
            visited = set()
            stack.append((x,y))
            visited.add((x,y))
            neighbors= [(0,1),(0,-1),(-1,0),(1,0)]
            while stack:
                x,y = stack.pop()
                if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1:
                    continue
                if grid[x][y] == 1:
                    # print(x,y, grid[x][y])
                    permieter_count += check_borders(x,y)
                    # print(permieter_count)
                    # print("land, adding to stack")
                    for x1,y1 in neighbors:
                        if (x+x1, y+y1) not in visited:
                            stack.append((x+x1, y+y1))
                            visited.add((x+x1, y+y1))

            return permieter_count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = dfs(i,j)
                    return count
                    
                
                    
                
                
                    
            