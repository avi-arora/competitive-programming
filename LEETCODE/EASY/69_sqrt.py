class Solution:
    def mySqrt(self, x: int) -> int:
        for guess in range(1,x):
            if guess * guess == x:
                return guess
            elif guess * guess > x:
                return guess-1
        return -1
    
    def mySqrtEfficient(self, x: int) -> int:
        pass

    

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))