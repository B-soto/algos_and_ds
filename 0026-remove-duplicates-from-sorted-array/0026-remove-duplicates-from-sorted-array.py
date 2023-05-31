class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x+=1
        return x
                      
#         [0,0,1,1,1,2,2,3,3,4]
#         [0,_,1,_,_,2,_,3,_,4]
        
#         [0,1,2,3]
        
        