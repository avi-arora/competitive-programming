
class Solution:
    def myPowNaive(self, x: float, n: int) -> float:
        """
        TLE - time limit exceed
        Compute X^n iteratively 
        TC: O(n)
        SC: (1)
        """
        i = 0
        result = 1
        while i < abs(n):
            result *= x
            i+=1
        if n < 0:
            return 1/result
        
        return result

        def myPow(self, x: float, n: int) -> float:
            pass

if __name__ == "__main__":
    pass
            
        