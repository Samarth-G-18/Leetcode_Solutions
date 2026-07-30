class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)         # Keep track of cheapest buy price
            profit = price - min_price                 # Profit if we sell today
            max_profit = max(max_profit, profit)       # Keep track of best profit
            
        return max_profit

        