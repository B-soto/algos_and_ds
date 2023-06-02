class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix)-1
        # t,b = 0, len(matrix)-1
        
        while l < r:
            for i in range(r-l):
                top = l
                bottom = r
                
                #top left -> top r
                temp = matrix[top+i][r]
                matrix[top+i][r] = matrix[top][l+i]
                
                
                #top right -> bottom right
                temp2 = matrix[bottom][r-i]
                matrix[bottom][r-i] = temp
                
                #bottom right -> botom left
                temp3 = matrix[bottom-i][l]
                matrix[bottom-i][l] = temp2
                
                
                # bottom left -> top left
                matrix[top][l+i] = temp3
            
                for row in matrix:
                    print(row)
                
            l += 1
            r -= 1
            
                
                
                
            
                
            
        
        