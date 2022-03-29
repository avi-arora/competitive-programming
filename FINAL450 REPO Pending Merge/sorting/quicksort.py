

def quickSort(arr, startIndex, endIndex):
    if startIndex < endIndex:
        #sort the pivot element and get index of pivot element
        #pivot = partition(arr, startIndex, endIndex-1,endIndex)
        pivot = partitionSingleWay(arr, startIndex, endIndex-1, endIndex)
        #sort left half of pivot
        quickSort(arr, startIndex, pivot-1)
        #sort right half of pivot 
        quickSort(arr, pivot+1, endIndex)


def partition(arr, startIndex, endIndex, pivot):
    while True:
        while arr[startIndex] < arr[pivot]:
            startIndex+=1
        
        while endIndex > 0 and arr[endIndex] > arr[pivot]:
            endIndex-=1
        
        if startIndex >= endIndex:
            break
        else:
            arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]

    #swap pivot with start index
    arr[startIndex], arr[pivot] = arr[pivot], arr[startIndex]
    #return pivot position
    return startIndex


def partitionSingleWay(arr, startIndex, endIndex, pivot):
    i, j = startIndex - 1, startIndex
    while j <= endIndex:
        if arr[j] < arr[pivot]:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
        j+=1
    #swap with pivot element
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1 
    


if __name__ == "__main__":
    arr = [35,33,42,10,14,19,27,44,26,31]
    print(arr)
    #partition(arr, 0, len(arr)-2, len(arr)-1)
    quickSort(arr, 0, len(arr)-1)
    print(arr)