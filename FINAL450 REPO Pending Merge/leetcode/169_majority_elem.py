class Solution:
    def majorityElement(self, nums: []) -> int:
        """
        Using Moore's Voting Algorithm
        TC: O(N)
        SC: O(1)
        """

    def majorityElementNaive(self, nums: []) -> int:
        """
        Naive algorithm 
        Algo
        1. create a dictionary containing frequecy of each elem and it's count
        2. return max frequency elem 
        TC: O(N)
        SC: O(N)
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for key, value in freq.items():
            if value > len(nums)//2:
                return key 

    def majorityElementUsingBST(self, nums: []) -> int:
        pass

    def majorityElementBruteForce(self, nums: []) -> int:
        pass

        
        
                



    


if __name__ == "__main__":
    obj = Solution()
    print(obj.majorityElementNaive([3,2,3]))