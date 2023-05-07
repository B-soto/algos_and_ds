class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
       
        def minCost(i):
            
            if i in cache:
                return cache[i]
            
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            
            left = minCost(i-1)
            right = minCost(i-2)
            
            total = cost[i] + min(left,right)
            
            
            cache[i] = total
            return total
            
        
        left = minCost(n-1)
        right = minCost(n-2)
        
        return min(left,right)