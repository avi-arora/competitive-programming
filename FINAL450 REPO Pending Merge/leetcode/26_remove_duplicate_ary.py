class Solution:
    def removeDuplicatesNaive(self, nums) -> int:
        """
        TLE: Time limit exceeded.
        TC: O(N^2) 
        SC: O(1)
        """
        for i in range(len(nums)):
            j = i
            #find the point 
            while j < len(nums)-1 and nums[j] == nums[j+1]:
                j+=1
            
            #j+1 is the diff point
            if j < len(nums)-1:
                j+=1
                while j > i+1:
                    nums[j-1] = nums[j]
                    j-=1
        i = 0
        while i < len(nums)-1 and nums[i] != nums[i+1]:
            i+=1
        print(nums)
        return i+1 #len of unique array


     def removeDuplicates(self, nums) -> int:
         """
         DIFF
         Two Pointer Approach
         TC: O(N)
         SC: O(1)
         """
         if len(nums) == 0: return 0
         i = 0
         for j in range(1, len(nums)):
             if nums[i] != nums[j]:
                 nums[i] = nums[j]
                 i+=1
        return i+1

if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicates([-2,-2,-1,-1,-1,0,1,2,2,3,3,3,4]))