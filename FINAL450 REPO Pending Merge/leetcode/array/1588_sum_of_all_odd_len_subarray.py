class Solution:
    def sumOddLengthSubarrays(self, arr: [int]) -> int:
        result = 0
        for x in range(1, len(arr)+1, 2):
            i, j = 0, x
            while j <= len(arr):
                result += sum(arr[i:j])
                i, j = i+1, j+1
        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.sumOddLengthSubarrays([10, 11, 12]))
