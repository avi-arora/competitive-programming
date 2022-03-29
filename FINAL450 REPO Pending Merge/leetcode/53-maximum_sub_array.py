

def maxSubArraySum(arr):
    """
    Using Brute Force 
    Algorithm
    1. Compute increasing subarrays
    2. compute sum of all increasing subarrays
    3. return max of sum of all increasing subarrays
    TC:O(N^3)
    Judge: TLE
    """
    #step 1
    subarr = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            temp = []
            for x in range(i, j+1):
                temp.append(arr[x])
            subarr.append(temp)
    
    #step 2 
    sums = [sum(x) for x in subarr]

    #step 3
    return max(sums)