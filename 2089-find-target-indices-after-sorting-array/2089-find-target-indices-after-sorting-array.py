class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        
        return [i for i in range(len(sorted_nums)) if sorted_nums[i] == target]