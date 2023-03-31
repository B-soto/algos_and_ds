class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0,len(height) -1
        
        
        while l < r:
            min_height = min(height[l], height[r]) 
            current_area = min_height * (r-l)
            max_area = max(max_area, current_area)
        
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
                
        return max_area
        
        