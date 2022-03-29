
def union_naive(arr1, arr2):
    result = []
    for x in arr1:
        if x not in result:
            result.append(x)
    for x in arr2:
        if x not in result:
            result.append(x)
    return result

def union_usingDict(arr1, arr2):
    result = {}
    for x in arr1:
        result[x] = x
    
    for x in arr2:
        result[x] = x
    
    return list(result.keys())


def intersection_naive(arr1, arr2):
    result = []
    for x in arr1:
        if x in arr2 and x not in result:
            result.append(x)
    return result

def intersection_usingDict(arr1, arr2):
    result = {}
    for x in arr1:
        if x in arr2:
            result[x] = x
    return list(result.keys())


if __name__ == "__main__":
    t = int(input())
    for x in range(t):
        
        n, m = map(int, input().split(" "))
        #a = [int(x) for x in input.split(" ")]
        #b = [int(x) for x in input.split(" ")]
        a = [int(input()) for x in range(n)]
        b = [int(input()) for x in range(m)]

        print(a)
        print(b)
        print(union_naive(a,b))
        print(union_usingDict(a,b))
        print(intersection_naive(a,b))
        print(intersection_usingDict(a,b))