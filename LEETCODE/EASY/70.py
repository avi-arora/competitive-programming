class Solution:
    def climbStairsBottomUp(self, n: int) -> int:
        #base cases
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

    def climbStairTopDown(self, n): 
        dp = {}
        def climbStair(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n not in dp:
                dp[n] = climbStair(n-1) + climbStair(n-2)
            return dp[n]
            
        return climbStair(n)
        