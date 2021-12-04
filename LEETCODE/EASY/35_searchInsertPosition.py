
def program():
    nums, key = [1,3,5,6], 2
    print(binarySearchRecursive(nums, 0, len(nums)-1,key))
    print(binarySearchIterative(nums, key))

def binarySearchRecursive(arr, start, end, key):
    if start > end:
        return -1
    middle = (start+end) // 2
    if arr[middle] == key:
        return middle
    elif arr[middle] > key:
        return binarySearchRecursive(arr, start, middle-1, key)
    elif arr[middle] < key:
        return binarySearchRecursive(arr, middle+1, end, key)
    else:
        return -1

def binarySearchIterative(arr, key):
    start, end = 0, len(arr)-1
    middle = 0
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            start = middle + 1
        elif arr[middle] > key:
            end = middle - 1
        else:
            return middle+1
    if key > arr[middle]:
        return middle + 1
    else:
        return middle



if __name__ == "__main__":
    program()