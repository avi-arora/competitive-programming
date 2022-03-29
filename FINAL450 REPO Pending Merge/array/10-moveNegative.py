
def usingPartition(arr, startIndex, endIndex):
    i, j = startIndex-1, startIndex
    while j <= endIndex:
        if arr[j] < 0:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
        j+=1
    return arr



def usingTwoPointerApproach(arr, startIndex, endIndex):
    while True:
        while arr[startIndex] < 0:
            startIndex+=1
        while endIndex >= 0 and arr[endIndex] >= 0:
            endIndex-=1
        if startIndex >= endIndex:
            break
        else:
            arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]
            startIndex+=1
            endIndex+=1
    return arr



if __name__ == "__main__":
    arr = [3,10,-2,-5,10,-1,8,-5,9]
    print(arr)
    #usingPartition(arr, 0, len(arr)-1)
    usingTwoPointerApproach(arr, 0, len(arr)-1)
    print(arr)

