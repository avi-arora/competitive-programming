

def reverse_naive(str):
    low, high = 0, len(str)-1
    strr = list(str)
    while low < high:
        strr[low], strr[high] = strr[high], strr[low]
        low, high = low+1, high-1
    return "".join(strr)



def reverse_py(str):
    return str[::-1]




if __name__ == "__main__":
    str = "anshu sharma"
    print(reverse_naive(str))