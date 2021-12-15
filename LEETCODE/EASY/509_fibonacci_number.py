class Solution:
    def fib(self, n: int) -> int:
        """
        >>> t.fib(2)
        1
        >>> t.fib(3)
        2
        >>> t.fib(4)
        3
        >>> t.fib(1)
        1
        >>> t.fib(0)
        0
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        def fibDP(n, dp):
            if n <= 0:
                return 0
            if n > 0 and n < len(dp) and dp[n] > 0:
                return dp[n]
            else:
                fib = fibDP(n-1, dp) + fibDP(n-2,dp)
                dp[n] = fib
                return fib
        return fibDP(n, dp)

    def fibRecursion(self, n: int) -> int:
        """
        >>> t.fibRecursion(2)
        1
        >>> t.fibRecursion(3)
        2
        >>> t.fibRecursion(4)
        3
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return self.fibRecursion(n-1) + self.fibRecursion(n-2)

    def fibIterative(self, n: int) -> int:
        """
        >>> t.fibIterative(2)
        1
        >>> t.fibIterative(3)
        2
        >>> t.fibIterative(4)
        3
        """
        fib0, fib1 = 0, 1
        fibNext = 0
        while n-1 > 0:
            fibNext = fib0 + fib1
            fib0, fib1 = fib1, fibNext
            n -= 1
        return fibNext






if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={"t": Solution()})