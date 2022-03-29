
def longest_palindromic_substring_bruteforce(s):
    """
    TC: O(N^3)
    SC: O(1)

    Computes longest palindromic substring using brute force. 
    """
    length = len(s)
    def getPalindromeLength(inputString):
        """
        TC: O(N//2) -> O(N)
        SC: O(1)
        
        Return length of plaindrome if inputString is palindrome else 0
        """
        length = len(inputString)
        i, j, isPalindrome = 0, length-1, True
        while i < (length//2):
            if inputString[i] != inputString[j]:
                isPalindrome = False
                break
            i, j = i+1, j-1
        return length if isPalindrome else 0

    maxLen, maxLenPalindrome = 0, ""
    for i in range(length):
        for j in range(length+1):
            currentPalindromeLen = getPalindromeLength(s[i:j])
            if currentPalindromeLen > 0 and currentPalindromeLen > maxLen:
                maxLen, maxLenPalindrome = currentPalindromeLen, s[i:j]
    
    return (maxLenPalindrome, maxLen)


            



if __name__ == "__main__":
    pass