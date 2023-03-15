class Solution:
    def __init__(self):
        self.cache = {}
    def uniquePaths(self, row: int, col: int) -> int:
        pair = (row,col)
        if pair in self.cache:
            return self.cache[pair]
        if row == col == 1:
            return 1
        if row < 1 or col < 1:
            return 0
        else:
            left = self.uniquePaths(row-1, col)
            right = self.uniquePaths(row, col-1)
        
        total_paths = left + right
        if pair not in self.cache:
            self.cache[pair] = total_paths
        return total_paths
        