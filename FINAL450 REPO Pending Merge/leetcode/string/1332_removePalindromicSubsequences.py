class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0: return 0
        else: return 1 if s == s[::-1] else 2
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.removePalindromeSub("bbaabaaa"))