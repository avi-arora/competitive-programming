

def checkPalindromeNaive(str):
    i, j = 0, len(str)-1
    flag = True
    while i < j:
        if str[i] != str[j]:
            flag = False
            break
        i, j = i+1, j-1

    return flag

def checkPalindromeRecursive(str, startIndex, endIndex):
    #one character string is always a palindrome
    if startIndex == endIndex:
        return True
    if str[startIndex] != str[endIndex]:
        return False
    
    if startIndex < endIndex+1:
        return checkPalindromeRecursive(str, startIndex+1, endIndex-1)
    
    return True




if __name__ == "__main__":
    str = input()
    print(checkPalindromeNaive(str))
    print(checkPalindromeRecursive(str, 0, len(str)-1))