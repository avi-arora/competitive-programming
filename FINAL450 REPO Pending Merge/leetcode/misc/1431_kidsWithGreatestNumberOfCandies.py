class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        currentMaxCandies = max(candies)
        result = []
        for c in candies:
            if c+extraCandies >= currentMaxCandies:
                result.append(True)
            else:
                result.append(False)
        
        return result
        
            




if __name__ == "__main__":
    obj = Solution()
    print(obj.kidsWithCandies([4,2,1,1,2],1))