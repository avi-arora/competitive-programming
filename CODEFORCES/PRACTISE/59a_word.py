def program():
    inputString = input()
    countUpper, countLower = 0, 0
    for c in inputString:
        if c.isupper():
            countUpper += 1
        else:
            countLower += 1
    if countUpper > countLower:
        return inputString.upper()
    else: 
        return inputString.lower()




if __name__ == "__main__":
    print(program())