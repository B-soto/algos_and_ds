class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_nums = []
        for row in matrix:
            all_nums += row
        
        sorted_nums = sorted(all_nums)
        
        return sorted_nums[k-1]
        