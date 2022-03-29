
def rev_pythonway(list):
    return list[::-1]

def rev_extraspace(list):
    result = [0] * len(list)
    i, j = 0, len(list)-1
    while i < len(list):
        result[j] = list[i]
        i+=1
        j-=1
    return result

def rev_usingswap(list):
    i, j = 0, len(list)-1
    while i < len(list)//2:
        list[i], list[j] = list[j], list[i]
        i+=1
        j-=1
    return list

def rev_recursion(list, start, end):
    if start >= end:
        return
    list[start], list[end] = list[end], list[start]
    rev_recursion(list, start+1, end-1)




if __name__ == "__main__":
    list = [1,2,3,4,5,6]
    print(rev_pythonway(list))
    list = [1,2,3,4,5,6]
    print(rev_extraspace(list))
    list = [1,2,3,4,5,6]
    print(rev_usingswap(list))
    list = [1,2,3,4,5,6]
    print(list)
    rev_recursion(list, 0, len(list)-1)
    
    print(list)
