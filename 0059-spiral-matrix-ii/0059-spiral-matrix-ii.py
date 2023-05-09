class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        matrix = [[0 for x in range(n)] for x in range(n)]
        # print(matrix)
           # r
#        l 
#          1 2
#       tb 4 3
        
        num = 1
        while left <= right and top <= bottom:
            
            for i in range(left,right+1):
                matrix[top][i] = num
                num +=1
            top +=1
            
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num +=1
                
            right -=1
            
            if not(left <= right and top <= bottom):
                break
                
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num +=1
                
            bottom -=1
            
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num +=1
                
            left +=1
            
        
        return matrix
            
                