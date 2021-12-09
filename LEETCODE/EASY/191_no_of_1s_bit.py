from typing import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        f, c = 1, 0
        while n > 0:
            if n & f == 1:
                c += 1
            n = n >> 1
        return c
    
    def hammingWeightFast(self, n:int) -> int:
        c = 0
        while n > 0:
            n = n & (n-1)
            c+=1
        return c
    





if __name__ == "__main__":
    s = Solution()
    n = int(input())
    print(s.hammingWeight(n))