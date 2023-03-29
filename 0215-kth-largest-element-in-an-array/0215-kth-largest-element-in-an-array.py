class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_arr = sorted(nums)
        return sorted_arr[-k]
        