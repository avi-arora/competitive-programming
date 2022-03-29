
def palindromeUsingString(number):
    """
    Convert number into string then check for palindrome.
    TC: O(n)
    SC: O(1)
    """
    if number < 0: return False
    str = number.__str__()
    si, ei = 0, len(str)-1
    while si <len(str) // 2:
        if str[si] != str[ei]:
            return False
        si, ei = si+1, ei-1  
    return True

def palindromeUsingIntReverse(number):
    """
    Reverse integer using math
    TC: O(n)
    SC: O(1)
    """
    if number < 0: 
        return False
    numLen, temp = 0, number
    while temp > 0:
        numLen, temp = numLen+1, temp//10
    
    revNumber, temp = 0, number
    while temp > 0:
        revNumber, temp = revNumber + (temp%10 * pow(10, numLen-1)), temp//10
        numLen -= 1
    
    if number == revNumber:
        return True
    return False


if __name__ == "__main__":
    print(palindromeUsingString(-121))
    print(palindromeUsingIntReverse(-121))