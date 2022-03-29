
def mergeSorted(arr1, m, arr2, n):
    #copy m into temp storage
    temp = arr1[:m+1]
    i, j , k = 0, 0, 0
    while i < m and j < n:
        if temp[i] < arr2[j]:
            arr1[k] = temp[i]
            i, k = i+1, k+1
        else:
            arr1[k] = arr2[j]
            j, k = j+1, k+1

    while i < m:
        arr1[k] = temp[i]
        i, k = i+1, k+1

    while j < n:
        arr1[k] = arr2[j]
        j, k = j+1, k+1

    return arr1
            
            


if __name__ == "__main__":
    print(mergeSorted([1,2,3,0,0,0],3,[2,5,6], 3))