class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff, xor = 0, x^y
        while xor > 0:
            diff += 1
            xor = xor & (xor-1)
        return diff




if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(1,4))