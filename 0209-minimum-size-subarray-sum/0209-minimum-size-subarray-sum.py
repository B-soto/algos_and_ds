class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       
        if sum(nums) < target:
            return 0
        
        curr_total = 0
        span = len(nums)
        l,r = 0,0
        
        # iterate over the nums list until we have cobined sum > target
            # calculate the span from left to right of the nums to reach target
            
            #while, we combined_sum greater than target
            
       
            
        while r < len(nums):
            curr_total += nums[r]
            
            if curr_total >= target:
                curr_span = (r - l) +1
                span = min(span, curr_span)
                
            while curr_total >= target:
                curr_total -= nums[l]
                l +=1
                if curr_total >= target:
                    curr_span = (r - l) +1
                    span = min(span, curr_span)
                    
            
            r +=1
            
            
        return span