
def findDuplicate_floyd(arr):
    """
    
    Find duplicate number in array using floyd cycle detection algorithm.
    
    TC: O(n)
    SC: O(1)
    
    we will do floyd detection in two phases
    phase 1: detect the cycle
    phase 2: point slow to start and point fast to where it was when cycle was detected, 
    move them 1 by 1, whem they met, it was the cycle entry point
    """
    #phase 1
    slow = fast = arr[0]
    while True:
        slow, fast = arr[slow], arr[arr[fast]]
        if slow == fast:
            break
    #phase 2
    slow = arr[0]
    while slow != fast:
        slow, fast = arr[slow], arr[fast]
    
    return fast # or slow 
    

def findDuplicateUsingSet(arr):
    """
    find duplicate using set
    TC: O(n)
    SC: O(n)
    """
    s = set([])
    for x in range(len(arr)):
        if arr[x] in s:
            return arr[x]
        s.add(arr[x])

    return -1


def findDuplicateUsingSorting(arr):
    """
    check for duplicate using sorting. 
    using merge sort
    TC: O(nlogn)
    SC: O(n), stack size and also temporary space.
    """
    pass

def mergeSort(arr, start, end):
    if start >= end:
        return 
    middle = (start + (end-start)) // 2
    mergeSort(arr, start, middle)
    mergeSort(arr, middle+1, end)
    merge(arr, start, end)

def merge(arr, start, end):
    """
    Two approaches to solve, 
    1. taking two arrays
    2. taking one array 
    """
    pass


if __name__ == "__main__":
    arr = [2,6,4,1,3,1,5]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)
    # print(findDuplicateUsingSet(arr))
    # print(findDuplicate_floyd(arr))
    

