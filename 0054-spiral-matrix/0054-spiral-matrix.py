class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output_arr = []
        
#           l r
#           123
#         t 456
#         b 789
        
        
        l = 0
        r = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while l < r and top < bottom:
            
            for i in range(l,r):
                output_arr.append(matrix[top][i])
            # print(output_arr)
            top += 1
            
            for i in range(top,bottom):
                output_arr.append(matrix[i][r-1])
            # print(output_arr)    
            r -=1
            
            if not l < r or not top < bottom:
                break
            
            for i in range(r, l, -1):
                output_arr.append(matrix[bottom-1][i-1])
            # print(output_arr)    
            bottom -= 1
                
            for i in range(bottom, top, -1):
                output_arr.append(matrix[i-1][l])
            # print(output_arr)
            l += 1            
            
        return output_arr