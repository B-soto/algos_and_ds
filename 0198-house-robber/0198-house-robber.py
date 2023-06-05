class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        
        def dfs(index):
            if index in cache:
                return  cache[index]
            if index >= len(nums):
                return 0
            if index == len(nums)-1:
                return nums[index]
            
            left = nums[index] + dfs(index+2)
            right = dfs(index+1)
            cache[index] = max(left,right)
            return max(left,right)
                
        max_rob = dfs(0)
        return max_rob
        
        
#                    i=0
        
#         /                  \
#      i=2                   i=1
#     /   \                    \
#  X i=4   i = 3 $                i =2
#                                     \
#                                     i=3
                                        
            
            