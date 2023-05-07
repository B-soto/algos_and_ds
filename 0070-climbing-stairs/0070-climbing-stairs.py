class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return n
        table = [0 for x in range(n)]
        table[0]= 1
        table[1]= 2
        
        for i in range(2,n):
            table[i] = table[i-1]+ table [i-2]
        return table [-1]
        
#         cache = {}
#         def dfs(s):
            
#             if s in cache:
#                 return cache[s]
#             if s < 0:
#                 return 0 
#             if s == 0 :
#                 return 1
            
#             left = dfs(s -1)
#             right = dfs(s -2)
            
#             cache[s] = left+right
            
#             return left + right
        
#         total_ways = dfs(n)
#         return total_ways
                