class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
            seen_set = {}
            # [2,7,11,15]
            
            for i in range(len(nums)):
                num = nums[i]
                comp_value = target - num
                
                if comp_value in seen_set:
                    return [i, seen_set[comp_value]]
                else:
                    seen_set[num] = i
            
            
            
        