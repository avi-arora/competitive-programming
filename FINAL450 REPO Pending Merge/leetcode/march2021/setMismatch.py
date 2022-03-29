class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        dic = {}
        n = len(nums)
        sum = (n*(n+1))//2
        duplicate = None
        for n in nums:
            if n in dic:
                duplicate = n
            dic[n] = 0
            sum-=n
        
        return [duplicate, duplicate + sum]


if __name__ == "__main__":
    obj = Solution()
    print(obj.findErrorNums([1,2,2,4]))