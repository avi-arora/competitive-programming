

def cycleRotateBruteForce(arr, n):
    for x in range(n):
        cycleRotateByOne(arr)
    return arr


def cycleRotateByOne(arr):
    i,elem = len(arr)-1, arr[len(arr)-1]
    while i > 0:
        arr[i] = arr[i-1]
        i-=1
    arr[i] = elem


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(cycleRotateBruteForce(arr,2));