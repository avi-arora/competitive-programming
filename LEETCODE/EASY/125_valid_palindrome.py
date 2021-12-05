class Solution:
    def isPalindrome(self, s: str) -> bool:
        #sanitize 
        s = ''.join([e.lower() for e in s if e.isalnum()])
        reversedString = s[::-1]
        if s == reversedString:
            return True
        return False



if __name__ == "__main__":
    s = Solution()
    string = input()
    print(s.isPalindrome(string))
