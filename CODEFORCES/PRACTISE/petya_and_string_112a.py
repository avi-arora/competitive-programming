def program():
    str1 = input()
    str2 = input()
    print(compareStrings(str1, str2))


def compareStrings(str1, str2):
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if(ord(str1[i].upper()) > ord(str2[j].upper())):
            return 1
        elif (ord(str1[i].upper()) < ord(str2[j].upper())):
            return -1
        i, j = i+1, j+1
    return 0




if __name__ == "__main__":
    program()