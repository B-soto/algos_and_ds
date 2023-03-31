class Solution:
    def maxArea(self, height: List[int]) -> int:
        #No Empty arr, at least 2 at all times so a valid area should be returned
        # [1,8,6,2,5,4,8,3,7] producs [.8......7]
        # So max is 7 * distance of 7 = 49.
        
        
        #Sudo Code 
        '''
        for every vertial line, calculate the area for every possible oppurunuity, and return the max. 
        Time BO(n^2) 
        
        max_area = 0 # return this late
        
        loop over height array
        min_height = min(height[l], height[r]) 
        current_area = height(min_height) * Width(r-l) 
        
        if current_area > max_area:
        update max area
        
        if l is < Right:
        then update left
        else if right is less than L, lower Irght
    
        
        [1,8,6,2,5,4,8,3,7]
            L       
                     R
                     
        big O(n) 
        Space o(1)
        '''
        max_area = 0
        l,r = 0,len(height) -1
        # r = len(height) -1
        
        
        while l < r:
            min_height = min(height[l], height[r]) 
            current_area = min_height * (r-l)
            max_area = max(max_area, current_area)
        
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
                
        return max_area
        
        