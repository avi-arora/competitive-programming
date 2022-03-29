def usingCountApproach(arr):
    zeroCount, oneCount, twoCount = 0,0,0
    for x in arr:
        if x == 0:
            zeroCount+=1
        elif x == 1:
            oneCount +=1
        else:
            twoCount+=1
    
    for x in range(len(arr)):
        if zeroCount > 0:
            arr[x] = 0
            zeroCount-=1
        elif oneCount > 0:
            arr[x] = 1
            oneCount-=1
        else:
            arr[x] = 2
            twoCount-=1
    return arr

def usingDutchNationalFlagAlgo(arr):
    i,low, mid, high = 0, 0, 0, len(arr)-1
    while mid <= high:
        if arr[i] == 0:
            #swap with mid
            arr[low], arr[mid] = arr[mid], arr[low]
            i, low, mid = i+1, low+1, mid+1
        elif arr[i] == 1:
            i, mid = i+1, mid+1
        elif arr[i] == 2:
            arr[high], arr[i] = arr[i], arr[high]
            high-=1
    
    return arr
    


if __name__ == "__main__":
    arr = [2,1,0,0,1,0,2,0,2,2,1,0,1]
    print(arr)
    #print(usingCountApproach(arr))
    print(usingDutchNationalFlagAlgo(arr))