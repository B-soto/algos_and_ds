class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         total = 0
        
#         [7,1,5,3,6,4]
#         i
#          i+1 is greater? If so, get the difference and add it to toal
#             else
#             moveon
            
        # [7,1,5,3,6,4]
                     
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] -prices[i-1]
        return profit
        