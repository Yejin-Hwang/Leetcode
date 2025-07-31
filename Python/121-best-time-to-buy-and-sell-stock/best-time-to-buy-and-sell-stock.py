class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0 
        for pri in prices: 
            if pri<min_price: 
                min_price = pri 
            elif  pri - min_price>max_profit: 
                max_profit = pri-min_price
        return max_profit
        