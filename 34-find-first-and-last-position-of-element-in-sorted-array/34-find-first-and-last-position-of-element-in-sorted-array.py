class Solution:
    def binary_search(self, arr: List[int], target: int) -> int:        
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = ((r-l) //2) + l            
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid-1
            else:
                l = mid+1
                
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # print('starting')
        if len(nums) == 0 or target not in set(nums):
            return [-1,-1]
        target_found_at_index = self.binary_search(nums,target)
        # print(target_found_at_index)
        start = target_found_at_index
        end = target_found_at_index
        
        while start > 0 and nums[start-1] == target:
            start -= 1
        while end < len(nums)-1 and nums[end+1] == target:
            end += 1
        return [start,end]
            
        
        