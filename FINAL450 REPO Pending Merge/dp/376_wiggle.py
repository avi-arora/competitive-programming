class Solution:
    def wiggleMaxLengthBruteForce(self, nums: [int]) -> int:
        """
        Algorithm: 
        step 1. compute the wiggle array in extra space
        step 2. iterate all pairs while keeping track of max length of wiggle 
        step 3. return the result
        TC: 
        SC: 
        """
        #build wiggle array 
        wiggle = []
        for i in range(len(nums)-1):
            wiggle.append(nums[i+1]-nums[i])
        
        maxWiggleLen = 0
        isPositive = True if wiggle[0] > 0 else False
        for i in range(len(wiggle)-1):
            currentWiggleLen = 1
            for j in range (i+1, len(wiggle)):
                if wiggle[j] < 0 and isPositive:
                    isPositive = not isPositive
                    currentWiggleLen += 1
                elif wiggle[j] > 0 and not isPositive:
                    isPositive = not isPositive
                    currentWiggleLen += 1
                else:
                    break
            if currentWiggleLen > maxWiggleLen:
                maxWiggleLen = currentWiggleLen
        
        return maxWiggleLen
                

    



if __name__ == "__main__":
    obj = Solution()
    print(obj.wiggleMaxLengthBruteForce([1,17,5,10,13,15,10,5,16,8]))