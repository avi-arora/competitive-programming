class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        while n > 0:
            c += 1
            n = n & (n-1)
        return True if c == 1 else False

    def isPowerOfTwoFast(self, n: int) -> bool:
        if n <= 0:
            return False
        if ((n & (n-1) == 0)):
            return True
        else:
            return False

if __name__ == "__main__":
    c = Solution()
    print(c.isPowerOfTwo(4))