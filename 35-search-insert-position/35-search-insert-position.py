class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        if target > arr[-1]: return len(arr)
        if target < arr[0]: return 0
        r = len(arr)-1
        l = 0
        
        while l <= r:
            mid = ((r - l) // 2) + l
            
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        
        return mid +1 if target > arr[mid] else mid
        