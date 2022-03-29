

def coinChangeRecursive(arr, size, n):
    #base case if n == 0 then we have a solution
    if n == 0:
        return 1
    elif size == 0 or n < 0: 
        return 0
    else: 
        return coinChangeRecursive(arr, size, n-arr[size-1]) + coinChangeRecursive(arr, size-1, n)

def coinChangeDP(arr, size, n):
    """
    """
    pass

if __name__ == "__main__":
    n, s = 4, [1,2,3]
    print(coinChangeRecursive(s, len(s), n))

