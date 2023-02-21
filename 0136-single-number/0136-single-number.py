class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        seen_set = {}
        for num in nums:
            if num in seen_set:
                seen_set[num] +=1
            else:
                seen_set[num] = 1
        for k,v in seen_set.items():
            if v == 1:
                return k
        