class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            
            if comp in seen_nums:
                return [seen_nums[comp], i]
            else:
                seen_nums[num] = i
                
        return False
    