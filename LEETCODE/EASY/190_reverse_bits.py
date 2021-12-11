class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_binary, count = 0, 0
        while n > 0:
            reverse_binary = (reverse_binary << 1) | (n&1)
            n = n >> 1
            count += 1
        reverse_binary = reverse_binary << 32-count
        return reverse_binary
    
    def reverseBitsUsingString(self, n: str) -> int:
        reverse_binary = ""
        while n > 0:
            reverse_binary += str(n%2)
            n = n//2
        for _ in range(0,32-(len(reverse_binary))):
            reverse_binary += "0"
        return int(reverse_binary,2)



if __name__ == "__main__":
    s = Solution()
    n = 43261596
    print(s.reverseBits(n))
    print(s.reverseBitsUsingString(n))