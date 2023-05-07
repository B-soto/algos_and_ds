class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(s):
            
            if s in cache:
                return cache[s]
            if s < 0:
                return 0 
            if s == 0 :
                return 1
            
            left = dfs(s -1)
            right = dfs(s -2)
            
            cache[s] = left+right
            
            return left + right
        
        total_ways = dfs(n)
        return total_ways
                