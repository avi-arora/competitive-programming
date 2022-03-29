
def reverseUsingBitMap(number):
    pass



def reverseInt(number):
    #count digits 
    flag = False
    if number < 0:
        flag = True
        number = -number
    digits, tempNum = 0, number
    while tempNum > 0:
        digits, tempNum = digits +1, tempNum // 10
    
    #reverse number
    revNum, tempNum = 0, number
    while tempNum > 0:
        revNum, tempNum = revNum + (tempNum % 10 * pow(10, digits -1)), tempNum // 10
        digits -= 1
    
    if flag:
        revNum = -revNum
    
    return revNum if revNum < pow(2,31)-1 and revNum > -pow(2,31)-1 else 0


if __name__ == "__main__":
    print(reverseInt(-12345))