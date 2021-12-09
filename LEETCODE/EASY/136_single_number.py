class Solution:
    def singleNumber(self, nums) -> int:
        pass
    
    def singleNumberUsingDict(self, nums) -> int:
        table = {}
        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
        
        for k, v in table.items():
            if v == 1:
                return k

    def singleNumberUsingAry(self, nums) -> int:
        temp = []
        for n in nums:
            if n in temp:
                temp.remove(n)
            else:
                temp.append(n)
        return temp[0]

        


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,2,3,1,1,5,9,5]
    print(s.singleNumberUsingDict(nums))
    print(s.singleNumberUsingAry(nums))