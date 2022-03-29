
def kth_minmax_usingsorting(list):
    """

    """
    pass

def kth_minmax(list):
    """
    """
    pass

def kth_usingquickselect(list,startIndex, endIndex, k):
    """
    uses quick select algorithm
    avg case: O(n)
    worst case: O(n^2)
    """
    def partition(arr, startIndex, endIndex):
        pivot = endIndex
        i, j = startIndex-1, startIndex
        while j <= endIndex:
            if arr[j] < arr[pivot]:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
            j+=1
        arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
        return i+1
    
    #condition for recursion doesn't exceed
    if k > 0 and k <= (endIndex - startIndex + 1):
        #get pivot position
        pivot = partition(arr, startIndex, endIndex)

        #base case 
        if pivot-startIndex == k-1:
            return arr[pivot]
        
        #pivot is large
        if pivot-startIndex > k-1:
            #recurse on left side
            return kth_usingquickselect(arr, startIndex, pivot-1, k)
        
        #recurse on right side
        return kth_usingquickselect(arr, pivot+1, endIndex, k-pivot+startIndex-1)
        
    return float("-inf")

if __name__ == "__main__":
    arr = [12, 5, 787, 1, 23]
    k=int(input())
    print(kth_usingquickselect(arr,0, len(arr)-1,k))

