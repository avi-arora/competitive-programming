class Solution:
    def countBits(self, n: int):
        result = []
        for i in range(n+1):
            c = 0
            while i > 0:
                c += 1
                i = i & (i-1)
            result.append(c)



if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))


