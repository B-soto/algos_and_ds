class Solution:
    def change(self, amount: int, AllCoins: List[int]) -> int:
        cache = {}
        
        def changeWays(total, coins):
            # print(str(coins))
            key = str(total) + '_' + str(coins)
            # print(key)
            if key in cache:
                return cache[key] 
            if total < 0:
                return 0
            if len(coins) == 0:
                if total > 0:
                    return 0
                else:
                    return 1
            
            left = changeWays(total-coins[-1], coins)
            
            last_coin = coins.pop()
            right = changeWays(total, coins)
            coins.append(last_coin)
            
            
            cache[key] = left+right
            return left + right
        
        totalWays = changeWays(amount, AllCoins)
        print(totalWays)
        return totalWays