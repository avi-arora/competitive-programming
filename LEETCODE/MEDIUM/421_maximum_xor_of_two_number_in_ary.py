class Solution:
    def findMaximumXORBruteForce(self, nums) -> int:
        """
        >>> t.findMaximumXORBruteForce([3,10,5,25,2,8])
        28
        >>> t.findMaximumXORBruteForce([0])
        0
        >>> t.findMaximumXORBruteForce([2,4])
        6
        >>> t.findMaximumXORBruteForce([8,10,2])
        10
        >>> t.findMaximumXORBruteForce([14,70,53,83,49,91,36,80,92,51,66,70])
        127
        """
        all_pairs = self.findAllPairBruteForce(nums)
        max_sum_xor = 0
        for pair in all_pairs:
            current_xor_sum = pair[0] ^ pair[1]
            if current_xor_sum > max_sum_xor:
                max_sum_xor = current_xor_sum
        return max_sum_xor

    def findAllPairBruteForce(self, nums):
        """
        >>> t.findAllPairBruteForce([1,2,3])
        [[1, 2], [1, 3], [2, 3]]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                result.append([nums[i], nums[j]])
        return result



if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t':Solution()})
        