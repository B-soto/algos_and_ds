class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) -1
        found_row = None
        found_col = None
        while left <= right:
            row_mid = ((right - left) //2) + left
            if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
                print(f"target found in row {matrix[row_mid]}")
                found_row = row_mid
                break
            elif target < matrix[row_mid][0]:
                right = row_mid -1
            else:
                left = row_mid +1
                
        if found_row is None:
            return False
        
        print("here")
        arr = matrix[found_row]
        l = 0
        r = len(arr)-1
        
        while l <= r:
            mid_col = ((r-l)//2) + l
            
            if arr[mid_col] == target:
                found_col = mid_col
                break
            elif arr[mid_col] > target:
                r = mid_col-1
            else:
                l = mid_col+1
        
        if found_col is None:
            return False
        else:
            return True
        
        
        