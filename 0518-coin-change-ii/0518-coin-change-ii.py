class Solution:
    def change(self, amount: int, AllCoins: List[int]) -> int:
        
        
#                                 5 [1,2,5]
#                                 /.    \
#                         0[1,2,5]      5[1,2]
#                       /      \
#             -5[1,2,5]       0[1,2]
#                                \ 
#                             0[1]
#                                 \ 
#                          -1[0]      0[]
        cache = {}
        def recurse(amount, AllCoins) -> int:
            key = str(amount) + "_" + str(AllCoins)
            
            if key in cache:
                return cache[key]
            if amount == 0 and len(AllCoins) == 0:                
                return 1
            if len(AllCoins) < 1:
                return 0
            if amount < 0:
                return 0 
            
            
            #recursive Case
            left = recurse(amount - AllCoins[-1], AllCoins)
            
            last_coin = AllCoins.pop()
            right = recurse(amount, AllCoins)
            AllCoins.append(last_coin)
            
            
            if key not in cache:
                cache[key] = right + left
            return right + left
            
        
        
        
        possible_ways = recurse(amount, AllCoins)
        return possible_ways
        