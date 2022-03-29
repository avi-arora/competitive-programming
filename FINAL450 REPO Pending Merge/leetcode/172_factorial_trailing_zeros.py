class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Computes no of trailing zero with help of below algorithm
        Algorithm
        1. compute floor (n/5^i) where i starts from 0 till floor(n/5^i) becomes zeros 
        2. stores the floor(n/5^i) in variable and increment in consecutive iterations 
        TC: O(N)
        SC: O(1)
        """
        totalZeros, i = 0, 1
        while True:
            val = n // pow(5,i)
            if val <= 0:
                break
            else:
                totalZeros += val
                i+=1
        return totalZeros


if __name__ == "__main__":
    obj = Solution()
    print(obj.trailingZeroes(5))
    