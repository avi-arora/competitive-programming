class Solution:
    def subsetXORSum(self, nums) -> int:
        pass

    def subsetXORSumBruteForce(self, nums) -> int:
        """
        >>> t.subsetXORSumBruteForce([5,1,6])
        28
        """
        sum = 0
        for counter in range(2**len(nums)):
            xor = 0
            for i in range(len(nums)):
                if(((counter) & 1 << i) > 0):
                    xor ^= nums[i]
            sum += xor
        return sum


    def iteratingAllSubset(self, nums):
        for counter in range(2**len(nums)):
            for i in range(len(nums)):
                #if ith bit of counter is set then print nums[i]
                if((counter & (1 << i)) > 0):
                    print(nums[i], end=",")
            print("\n")




if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={"t": Solution()})
    s = Solution()
    nums = []
    print(s.subsetXORSumBruteForce([5,1,6]))
    print(s.subsetXORSum(nums))



