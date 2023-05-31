class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
#         [1,1,2]
#         [1,2]
        
#         index = 5
#         [0,0,1,1,1,2,2,3,3,4]
#         [0,1,2,3,4]
        
        index = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
                
        return index
            
        
        