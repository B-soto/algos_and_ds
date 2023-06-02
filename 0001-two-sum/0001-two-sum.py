class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # seen_set = {2:1, 3:0, }
        
        # create a seen dictionary
        
        # iterate over our nums list, subtract num from target and see if complimentry value has been seen yet. 
        #If not add it to the dict
        #If so return the seen values
        
        
        # End of program return False
        
        seen_nums = {}
        
        for i in range(len(nums)):
            val = nums[i]
            comp = target - val
            
            if comp not in seen_nums:
                seen_nums[val] = i
            else:
                return [seen_nums[comp], i]
            
        