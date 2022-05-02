class Solution:
    def maxProfitBruteForce(self, prices) -> int:
        #GIVES TLE
        #brute force solution
        result = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i, n):
                if (prices[j] - prices[i]) > result:
                    result = prices[j] - prices[i]
        
        return result
    
    def maxProfitDP(self, prices) -> int:
        dp = [[0,0]] * len(prices)
        #setting up dp table
        # [min_price, max_profit]
        dp[0] = [prices[0], 0]
        for i in range(1, len(prices)):
            min_price = min(dp[i-1][0], prices[i])
            max_profit = max(dp[i-1][1], prices[i]-dp[i-1][0])
            dp[i] = [min_price, max_profit]
        
        return dp[len(prices)-1][1]
    
    def maxProfitEfficient(self, prices) -> int:
        max_profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[sell] - prices[buy] > max_profit:
                max_profit = prices[sell] - prices[buy]
            elif prices[buy] > prices[sell]:
                buy = sell
            sell+=1
        
        return max_profit
        
        
        