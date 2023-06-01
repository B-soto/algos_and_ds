class Solution:
    def coinChange(self, totalCoins: List[int], totalAmount: int) -> int:
        cache = {}
        
        
        
        
        def dfs(amount):
            if amount in cache:
                return cache[amount]
            
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            
            curr_min = float('inf')
            for coin in totalCoins:
                
                curr_min = min(dfs(amount - coin),curr_min)
            
            cache[amount] = curr_min +1
            return curr_min +1
            
            
        min_coin = dfs(totalAmount)
        if float('inf') == min_coin:
            return -1
        return min_coin
        
