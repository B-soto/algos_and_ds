#REWRITE, with (nlogn)... the set we are making is O(n)
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
        return -1
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]
        target_found_at_index = self.binary_search(nums,target)
        
        if target_found_at_index == -1:
            return [-1,-1]
        
        start, end = target_found_at_index, target_found_at_index
        
        while start > 0 and nums[start-1] == target:
            start -= 1
        while end < len(nums)-1 and nums[end+1] == target:
            end += 1
        return [start,end]
            
        
        