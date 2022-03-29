import sys

def largestSumBruteForce(arr):
    """
    LeetCode Easy -> Ques 53. 
    Algorithm
    1. find all subarrays
    2. find sum of all subarrays
    3. find largest/smallest from the sum of all subarrays
    TC: O(N^3) + O(N^2) + O(N) = O(N^3)
    SC: O(1)

    >>> largestSumBruteForce([-2,-3,4,-1,-2,1,5,-3])
    7
    >>> largestSumBruteForce([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> largestSumBruteForce([1])
    1
    >>> largestSumBruteForce([-1])
    -1
    """
    #step 1
    subarr = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            temp = []
            for x in range(i,j+1):
                temp.append(arr[x])
            subarr.append(temp)
    
    #step 2
    sums = [sum(x) for x in subarr]

    #step 3
    return max(sums)
            
def largestSumBruteForceSum(arr):
    """
    Above algorithm, all the steps in single loops

    >>> largestSumBruteForceSum([-2,-3,4,-1,-2,1,5,-3])
    7
    >>> largestSumBruteForceSum([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> largestSumBruteForceSum([1])
    1
    >>> largestSumBruteForceSum([-1])
    -1
    """
    maxSum = -sys.maxsize
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            tempSum = 0
            for k in range(i, j+1):
                tempSum += arr[k]
            maxSum = max(maxSum, tempSum)

    return maxSum


def maxContiguousSumSubArrayUsingPrefix(arr):
    """
    Computes the maximum sum contiguous subarray using the prefix array approach
    Algorithm
    1. compute a prefix array
    2. compute range sum of i to j using formulae rangeSum = prefix[j] - prefix[i] + arr[i]
    3. compare with maxSum continuously and maintain max sum
    TC: O(N^2)
    SC: O(N)


    >>> maxContiguousSumSubArrayUsingPrefix([-2,-3,4,-1,-2,1,5,-3])
    7
    >>> maxContiguousSumSubArrayUsingPrefix([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> maxContiguousSumSubArrayUsingPrefix([1])
    1
    >>> maxContiguousSumSubArrayUsingPrefix([-1])
    -1

    """     
    #step 1
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    #step 2
    maxSum = -sys.maxsize
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            tempSum = prefix[j] - prefix[i] + arr[i]
            maxSum = max(maxSum, tempSum)
    #step 3
    return maxSum
      

def largestSumUsingDAC(arr, start, end):
    """
    TC: 
    SC:
    """
    pass

def largestSumUsingKadane(arr):
    """
    TC: O(N)
    SC: O(1)
    >>> largestSumUsingKadane([-2,-3,4,-1,-2,1,5,-3])
    7
    >>> largestSumUsingKadane([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> largestSumUsingKadane([1])
    1
    >>> largestSumUsingKadane([-1])
    -1
    >>> largestSumUsingKadane([47, 43, 94, -94, -93, -59, 31, -86])
    137
    """
    max_so_far, max_till_now = -sys.maxsize, 0
    for i in range(len(arr)):
        max_till_now = max_till_now + arr[i]
        if max_so_far < max_till_now:
            max_so_far = max_till_now
        if max_till_now < 0:
            max_till_now = 0
    return max_so_far


if __name__ == "__main__":
    arr = [1,-2,-3,4]
    print(maxContiguousSumSubArrayUsingPrefix(arr))
   # print(largestSumBruteForce(arr))
    #print(largestSumBruteForce([-2,1,-3,4,-1,2,1,-5,4]))
    