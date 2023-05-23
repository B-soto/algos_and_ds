class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money = 0
        
        for row in accounts:
            total = sum(row)
            max_money = max(max_money, total)
        return max_money
        